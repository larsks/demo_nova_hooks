#!/usr/bin/python


class SimpleHookCreate (object):

    logfile = '/var/log/nova/hook-create.log'

    def pre(self, *args, **kwargs):
        with open(self.logfile, 'a') as fd:
            print >>fd, 'BEGIN PRE'
            for i, arg in enumerate(args):
                print >>fd, '%d: %s' % (i, arg)
            for k, v in kwargs.items():
                print >>fd, '%s=%s' % (k, v)
            print >>fd, 'END PRE'

    def post(self, *args, **kwargs):
        with open(self.logfile, 'a') as fd:
            print >>fd, 'BEGIN POST'
            for i, arg in enumerate(args):
                print >>fd, '%d: %s' % (i, arg)
            for k, v in kwargs.items():
                print >>fd, '%s=%s' % (k, v)


class SimpleHookNetwork (object):

    logfile = '/var/log/nova/hook-network.log'

    def pre(self, *args, **kwargs):
        with open(self.logfile, 'a') as fd:
            print >>fd, 'BEGIN PRE'
            for i, arg in enumerate(args):
                print >>fd, '%d: %s' % (i, arg)
            for k, v in kwargs.items():
                print >>fd, '%s=%s' % (k, v)
            print >>fd, 'END PRE'

    def post(self, *args, **kwargs):
        with open(self.logfile, 'a') as fd:
            print >>fd, 'BEGIN POST'
            for i, arg in enumerate(args):
                print >>fd, '%d: %s' % (i, arg)
            for k, v in kwargs.items():
                print >>fd, '%s=%s' % (k, v)
            print >>fd, 'END POST'


class SimpleHookDelete (object):

    logfile = '/var/log/nova/hook-delete.log'

    def pre(self, *args, **kwargs):
        with open(self.logfile, 'a') as fd:
            print >>fd, 'BEGIN PRE'
            for i, arg in enumerate(args):
                print >>fd, '%d: %s' % (i, arg)
            for k, v in kwargs.items():
                print >>fd, '%s=%s' % (k, v)
            print >>fd, 'END PRE'

    def post(self, *args, **kwargs):
        with open(self.logfile, 'a') as fd:
            print >>fd, 'BEGIN POST'
            for i, arg in enumerate(args):
                print >>fd, '%d: %s' % (i, arg)
            for k, v in kwargs.items():
                print >>fd, '%s=%s' % (k, v)
            print >>fd, 'END POST'
