Proof of concept for sending StatsD metrics to Monasca
======================================================

This is a barebones proof of concept for generating StatsD
metrics and sending them via UDP to the Monasca StatsD service
running in another container.

If required it could easily be extended to be independent of
the monitoring framework.

Usage
-----

The Monasca StatsD service must be resolvable by DNS from
this proof of concept container. This example assumes
that the hostname of the Monasca StatsD service is
`monasca-agent-statsd`, and adds an entry to the `/etc/hosts`
file in the proof of concept container using the docker
`--link` option:

`docker run -d --link monasca-agent-statsd stackhpc/statsd-demo`
