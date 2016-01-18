---
layout: post
title: Tomcat Shutdown Issues Caused by Embedded Infinispan Cache
date: '2016-01-18 21:06:17'
---

I was recently stumped by some shutdown issues in a Tomcat-hosted Java webservice. The server just wouldn't shut down cleanly. After (most of) a day running round in circles, I tracked the issue down to embedded <a href="http://infinispan.org/" target="_blank">Infinispan</a> - and specifically <a href="http://jgroups.org/" target="_blank">JGroups</a>.

I'm writing the solution up here in the hopes someone might find it useful.

###Background

To ensure a proper resource cleanup during JVM shutdown, Infinispan has built in <a href="https://docs.jboss.org/infinispan/7.1/apidocs/org/infinispan/configuration/global/ShutdownHookBehavior.html" target="_blank">shutdown hooks</a>. Tomcat (and most other Application Servers) have their own shutdown hooks, so it's desirable to turn off Infinispan's built-in shutdown hooks to prevent any contention issues. Via <code>infinispan.xml</code>:

{% highlight xml %}
<infinispan
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="urn:infinispan:config:7.0 http://www.infinispan.org/schemas/infinispan-config-7.0.xsd"
    xmlns="urn:infinispan:config:7.0">

   <cache-container default-cache="default" shutdown-hook="DONT_REGISTER">
       <local-cache name="xml-configured-cache">
          <eviction strategy="LIRS" max-entries="10" />
       </local-cache>
   </cache-container>

</infinispan>
{% endhighlight %}

###The Issue

When Infinispan running in a <a href="http://infinispan.org/docs/7.0.x/user_guide/user_guide.html#_clustered_configuration" target="_blank">clustered configuration</a>, it uses <a href="http://jgroups.org/" target="_blank">JGroups</a> for network communications.

By unregistering the shutdown hooks (as above), non-daemon JGroups threads are left running inside the Application Server - even after a shutdown call. This prevents the Application Server process from terminating - it needs to be killed. From <a href="http://docs.oracle.com/javase/7/docs/technotes/tools/share/jstack.html" target="_blank">jstack</a>, the culprit threads are:

* INT-1
* INT-2
* multicast receiver
* unicast-receiver
* TransferQueueBuilder

The question: how do we stop these runaway threads and allow the Application Server to shutdown gracefully?

###The Fix

The fix is fairly simple.

Being a <a href="https://en.wikipedia.org/wiki/Web_container" target="_blank">Servlet Container</a>, Tomcat conforms to the <a href="http://docs.oracle.com/javaee/6/api/javax/servlet/Servlet.html" target="_blank">Java Servlet API</a>. We can use the <a href="https://docs.oracle.com/javaee/6/api/javax/servlet/ServletContextListener.html" target="_blank">ServletContextListener Interface</a> to initiate a graceful Infinispan shutdown when Tomcat shutdown is initiated. Using <a href="https://spring.io/" target="_blank">Spring</a>:

{% highlight java %}
@WebListener
public class ContextFinalizer implements ServletContextListener {

    ...

    @Override
    public void contextDestroyed(ServletContextEvent servletContextEvent) {
        DefaultCacheManager cacheManager = (DefaultCacheManager) ContextLoaderListener.getCurrentWebApplicationContext().getBean("cacheManager"); // my cache manager bean is called "cacheManager"
        cacheManager.stop();
    }
}
{% endhighlight %}

That's all there is to it!

###Moral of the Story

When you unregister Infinispan shutdown hooks via <code>DONT_REGISTER</code>, **always make sure to manually stop the Infinispan caches via <code>CacheManager.stop()</code>**.

###References

* <a href="http://infinispan.org/docs/7.0.x/getting_started/getting_started.html" target="_blank">Getting Started with Infinispan</a>
* <a href="https://developer.jboss.org/thread/200640?db=5" target="_blank">how to use shutdownHookBehaviour</a>
* <a href="http://docs.jboss.org/infinispan/7.0/configdocs/infinispan-config-7.0.html" target="_blank">Infinispan 7.0 XML schema</a>
* <a href="https://docs.jboss.org/infinispan/7.1/apidocs/org/infinispan/configuration/global/ShutdownHookBehavior.html" target="_blank">Infinispan ShutdownHookBehavior</a>
* <a href="https://docs.oracle.com/javaee/6/api/javax/servlet/ServletContextListener.html" target="_blank">Interface ServletContextListener</a> 
