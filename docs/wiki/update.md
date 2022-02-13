---
title: Update the wiki
tags:
  - internal
  - procedure
---

# Update the wiki

This page contains information about how to update this wiki.
So in short, this wiki is a set of markdown pages in a [github repository](https://github.com/chordflower/chordflower), that uses:

- [mkdocs](https://www.mkdocs.org)
- [mkdocs-material](https://squidfunk.github.io/mkdocs-material)

In order to build a website that is then deployed to github pages, by a github action upon a commit in the develop branch.

## Building

If you want to do a local build of the wiki and have the repository files in hand, you need to first have before hand:

- [python >=3.10](https://www.python.org)
- [poetry >=1.1.7](https://python-poetry.org)
- Internet connection
- [moustache](https://en.m.wikipedia.org/wiki/Handlebar_moustache) or [moustache 2](https://en.m.wikipedia.org/wiki/Walrus_moustache)
- [brown sugar](https://open.spotify.com/track/5dGVIZ6oc0ScR4ldWGbXSU?si=fiT7C8gUTSqxNLf_3COERw)

**Note:** Do not mess with these [man](./badass_man.jpg).

Then in a shell type in:

```bash
poetry install
poetry run python scripts.py dist
```

And you should have the final result in the `dist` directory in the root directory.

To have a server version, you may also use:

TODO

And then open [http://localhost:8080](http://localhost:8080) to view the resulting website.

## Structure

All of the documentation is inside the docs folder as markdown files.
Also, in the static folder there is the files needed for the PWA application, like the favicons, manifest and service worker.

## License

This project and website content is licenses under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).
