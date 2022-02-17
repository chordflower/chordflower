---
title: Product
tags:
  - management
  - product
---

This page describes a product, including some of the its basic properties and what it must have to become in a stable (or proper) state.

## Properties

The properties common of a product are:

- name => The product name;
- description => A simple product description;
- version => The latest version of a product (must obey to the [semantic versioning standard](https://semver.org/spec/v2.0.0.html));
- area => The product [area](./areas.md);
- category[1..*] => The product [category](./areas.md) (can be 1 or more);
- license[1..*] => The product license as a [spdx string](https://spdx.org/licenses/) ( can be 1 or more);
- website => The product main website;
- repository => Information about the product repository:
  - name => A human readable name for the repository;
  - url => A human viewable url for the repository;
  - connection => A url for usage by a vcs (version control system):
    - read-only => A read-only url usable by a vcs;
    - read-write => A read-write url usable by a vcs (may require proper permissions);
- issues => Information about the product issue/feature tracker:
  - name => A human readable name for the issue/feature tracker;
  - url => A human viewable url for the issue/feature tracker;
- continuous_integration => Information about the product continuous integration system:
  - name => A human readable name for the product continuous integration system;
  - url => A human viewable url for the product continuous integration system;
- state => The current product state.

## Stable product features

A stable or proper product has the following features or things:

- Has it's code in a repository;
- Has a issue/feature tracker setup;
- Has a continuous integration system setup for it;
- When has a website with documentation about the project;
- The website includes the public API documentation in case of a library;
- It is able to be deployed or used by an end-user without a lot of effort;
- It has a current version bigger or equal to 1.0.0.
