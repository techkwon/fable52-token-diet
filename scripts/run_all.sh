#!/bin/zsh
cd <project>/samples
chainspec() { ./run.sh spec $1 && { ./run.sh build-opus $1 & ./run.sh build-sonnet $1 & ./run.sh build-gpt $1 & wait; }; }
chainspec motion &
chainspec lesson &
( ./run.sh fable-high motion; ./run.sh fable-high lesson ) &
( ./run.sh fable-low motion; ./run.sh fable-low lesson; ./run.sh opus-solo motion; ./run.sh opus-solo lesson ) &
wait; echo ALLDONE
