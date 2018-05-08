import statsd
import time
import random

statsd_client = statsd.StatsClient('monasca-agent-statsd', 8125, prefix='statsd')


@statsd_client.timer('foo.duration')
def _foo():
    statsd_client.gauge('foo.gauge',
                        random.randint(1, 100),
                        rate=1,
                        delta=False)
    print("Sleeping..")
    time.sleep(1)


if __name__ == "__main__":
    while True:
        _foo()
        statsd_client.incr('foo.called')
