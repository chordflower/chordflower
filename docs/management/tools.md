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
- eslint => Eslint is used to lint the code (this is present on the dev dependencies of the package, so no need for global installs);
- nps => So that there can be a file package-scripts which greatly eases the creation of npm scripts;
- mocha => As the testing framework with its BDD interface, along with:
  - chai => For expectations;
  - sinon => For mocks and spies;
- ts-node => For running the tests, along with **source-map-support**;
- typedoc => For producing documentation from the code;

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

#### Eslint

The following plugins are used:

- @typescript-eslint/eslint-plugin => The typescript plugin for eslint, this is used along with the corresponding parser;
- eslint-plugin-unicorn;
- eslint-plugin-jsdoc => This is specific to documentation;

### Frontend

For the frontend the languages used are:

- typescript => As referenced above, as replacement/complement to javascript;
- postcss => As a complement to css;

As for the tools:

- parcel => For bundling the code together;
- pitsby => For documenting interface components;
- Other tools already mentioned in typescript.

And for the libraries/frameworks:

- lodash => For some utilities;
- luxon => For handling with dates in a proper way;
- reflect-metadata and tslib => For typescript stuff;
- mathjs => For handling decimal numbers so that 0.2 + 0.1 = 0.3;
- vue.js 3.x => For the general webapp framework;
- vuex => For handling vue.js state;
- vue-router => For handling routes in vue.js;
- vue-i18n-next => For translation in vue.js
- forage => For using indexedDB;
- lit-element or lit => For creating components as web components;

As plugins for postcss:

- tailwindcss => The utility-first postcss framework;
- cssnano => For minimizing css;
- level4;
- postcss-import;
- postcss-nested;
- postcss-simple-extend.

### Golang


