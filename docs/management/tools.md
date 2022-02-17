---
title: Tools
tags:
  - management
  - tools
---

This page describes some tools commonly used by chordflower.

## Repository management

For repository management, [git](https://git-scm.com/) is used, together with github at the [chordflower](https://github.com/chordflower) space.

For generating a .gitignore file, the [gitignore.io](https://gitignore.io/) webapp is used.

## Issue/Feature tracker

For issue/feature tracking, the github issue tracker is used.

## Continuous integration

For continuous integration, there are two systems being used:

- github actions;
- travis.ci.

## Language Specific Tools

In this section, some language specific tools are listed.

### Typescript

Since typescript is also closely associated with node and its environments, some of these tools also apply to node development, after this, the tools used are:

- yarn > 3.1 or latest modern yarn => Yarn is used, instead of npm, more on this bellow;


#### Yarn

About yarn, some of its features used in ChordFlower are:
  - Workspaces => ChordFlower uses pure yarn workspaces, without lerna, because lerna sucks;
  - Plugins => In particular, the following plugins:
    - workspace-tools => If the project deals with workspaces, just this plugin KO's lerna by fatality with a flawless victory;
    - typescript => Obligatory if you use typescript and want to have types;
    - interactive-tools => To do ease updates of dependencies;

Also, the Plug and Play API is not used (yet), so there is a line:

~~~yaml
nodeLinker: "node-modules"
nmMode: "hardlinks-local"
~~~

In the file .yarnrc.yml in every repository.


