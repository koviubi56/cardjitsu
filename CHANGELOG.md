# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-beta.2] - 2021-03-19
### Added
- There are 2 settings you can set to `True` or `False` (you need to edit the file)
  - With colors, without colors
  - SPTGAL (Still play the game after loose)
### Changed
- The lose now in a function

## [1.0.0-beta.1] - 2021-03-17
### Added
- Now all functions have documentetion
### Changed
- All cards are now colorized
### Fixed
- Now there are no `raise RuntimeError`s!
- An error and a lose message was in the wrong place.

## [1.0.0-alpha.2] - 2021-03-16
### Added
- If you have no cards, you lose
- Now you can win, and lose the (whole) game
- Now you can have max 3 card in a type (water, fire, snow), if you have more than 3, you lose (if the robot have more than 3, you **win**)
- If you (or the robot) have 0 cards, you get more 10!
- If you get an error, you can see what's wrong (the error, and (if there is a variable) the variable)
### Changed
- If there is an if commands, now we specife every condition, also the last condition too (https://tknk.io/S1Pz)
- Now the userChoice variable is `{"type": userT, "level": userL, "color": userC}`, and we use the variable, and not write that long string
- Now you have 10 cards
### Removed
- The version print at the start of the code (`if __name__ == '__main__':`)
### Fixed
- The level of a card now can't be 0 (*replaced 0 with 1*)
- Now the used cards will be displayed (not just the water)
- Now you can see your winned snow cards (*replaced 2 with 3*)

## [1.0.0-alpha.1] - 2021-03-15
