# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-alpha.2] - 2021-03-16
### Added
- If you have no cards, you lose
- Now you can win, and lose the (whole) game
- Now you can have max 3 card in a type (water, fire, snow), if you have more than 3, you lose (if the robot have more than 3, you **win**)
### Changed
- If there is an if commands, now we specife every condition, also the last condition too (https://tknk.io/S1Pz)
- Now the userChoice variable is `{"type": userT, "level": userL, "color": userC}`, and we use the variable, and not write that long string
- Now you have 10 cards
### Removed
- The version print at the start of the code (`if __name__ == '__main__':`)
### Fixed
- The level of a card now can't be 0
- Now the used cards will be displayed (not just the water)

## [1.0.0-alpha.1] - 2021-03-15
