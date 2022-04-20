#!/bin/bash
shopt -s expand_aliases

alias   alice-cli="docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://alice-node:7770"
alias     bob-cli="docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://bob-node:7770"
alias charlie-cli="docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://charlie-node:7770"

printf "\n========= ALICE'S NODE ========="
printf "\nAlice's balance: "
alice-cli accounts balance alice --auth hi_alice
printf "Bob's balance: "
alice-cli accounts balance bob --auth hi_alice

printf "\n========= BOB'S NODE ========="
printf "\nAlice's balance: "
bob-cli accounts balance alice --auth hi_bob
printf "Charlie's balance: "
bob-cli accounts balance charlie --auth hi_bob

printf "\n========= CHARLIE'S NODE ========="
printf "\nBob's balance: "
charlie-cli accounts balance bob --auth hi_charlie
printf "Charlie's balance: "
charlie-cli accounts balance charlie --auth hi_charlie
