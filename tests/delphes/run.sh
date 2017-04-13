#!/usr/bin/env bash

packtivity-run -t from-github/phenochain delphes.yml \
  -p inputhepmc="$PWD/pythia/output.hepmc" \
  -p outputroot="'{workdir}/output.root'" \
  -p outputlhco="'{workdir}/output.lhco'" \
  -p delphes_card=delphes/cards/delphes_card_ATLAS.tcl \
  --read pythia --write outdir