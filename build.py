#!/usr/bin/python

# Gitless - a version control system built on top of Git.
# Copyright (c) 2013  Santiago Perez De Rosso.
# Licensed under GNU GPL, version 2.

"""Build Gitless package."""


import argparse
import compileall
import os
import re
import shutil
import stat

FILE_PERMISSIONS = (
    stat.S_IRUSR |  # Owner reads.
    stat.S_IWUSR |  # Owner writes.
    stat.S_IXUSR |  # Owner executes.
    stat.S_IRGRP |  # Group reads.
    stat.S_IXGRP |  # Group writes.
    stat.S_IROTH |  # Other reads.
    stat.S_IXOTH    # Other executes.
)


def main():
  parser = argparse.ArgumentParser(
      description="Build Gitless package")
  parser.add_argument('version', help='name of the version to package')

  args = parser.parse_args()

  rx = re.compile('build.py')

  cwd = os.getcwd()

  print 'Compiling all python files'
  # TODO(sperezde): compile with -OO.
  compileall.compile_dir(cwd, ddir=args.version, force=True, rx=rx)
  print 'Done compiling'

  print 'Creating dir %s' % args.version
  os.mkdir(args.version)
  print 'Dir created'

  for f in os.listdir(cwd):
    if f.endswith('.pyc'):
      new_path = os.path.join(args.version, f) 
      print 'moving file %s to %s' % (f, new_path)
      os.rename(f, new_path)
      _maybe_create_exec_file(f, args.version)

  _create_exec_file('gl', args.version, is_gl=True)

  gitpylib = os.path.join(cwd, 'gitpylib')
  gitpylib_dst = os.path.join(args.version, 'gitpylib')
  os.mkdir(gitpylib_dst)

  for f in os.listdir(gitpylib):
    if f.endswith('.pyc'):
      new_path = os.path.join(gitpylib_dst, f) 
      src_path = os.path.join('gitpylib', f)
      print 'moving file %s to %s' % (src_path, new_path)
      os.rename(src_path, new_path)

  print 'Done'


def _maybe_create_exec_file(f, dst):
  match = re.match('gl_(\w+).pyc', f)
  if match:
    cmd = match.group(1)
    _create_exec_file(cmd, dst)


def _create_exec_file(cmd, dst, is_gl=False):
  if is_gl:
    path = os.path.join(dst, cmd)
  else:
    path = os.path.join(dst, 'gl-' + cmd)
  print 'Creating exec file for %s at %s' % (cmd, path)
  f = open(path, 'a')
  f.write('#!/bin/bash\n')
  if is_gl:
    f.write('python /usr/local/gitless/bin/gl.pyc "$@"')
  else:
    f.write('python /usr/local/gitless/bin/gl_%s.pyc "$@"' % cmd)
  f.close()
  os.chmod(path, FILE_PERMISSIONS)
  print 'Done creating exec file for %s at %s' % (cmd, path)


if __name__ == '__main__':
  main()