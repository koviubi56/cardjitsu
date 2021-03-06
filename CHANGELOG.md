# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2021-04-18
### Fixed
- [Removed notImportant everywhere](https://github.com/koviubi56/cardjitsu/pull/19/commits/9c2efc114f7dbe6572e84dc05291ca7eb71a10e8)
- [Removed `0`s from `range()`s in `for` loops](https://github.com/koviubi56/cardjitsu/pull/19/commits/d2cb999cdb16f8ea6456d9ef47aa9f4e61c6f565)
- [Added `enumerate()`](https://github.com/koviubi56/cardjitsu/pull/19/commits/20a5d30c24f539342aeb163f0cb5bbbdae92bb4b)
- [Changed an error check](https://github.com/koviubi56/cardjitsu/pull/19/commits/3ce16ba2f553806298140b8064ca4a63c3797815)

## [1.2.0] - 2021-04-14
### Added
- Added ITALT10CGAC (If There Are Less Than 10 cards, than Give A Card)
- Added a `win` function
- Added `when100` to debug mode `pause`
### Removed
- Removed the `num` variable from the lose function
### Fixed
- The chosed card of player2 is now removed from its cards after using it

## [1.2.0-beta.1] - 2021-04-12
### Added
- Added debug mode
- Now there is a `testLose()`, and we use it
### Changed
- We tring to use `pass` and not notImportant
### Fixed
- Now you can play again after losing
- Now Player2 can just choose cards that it have

## [1.1.3] - 2021-04-11 
### Added
- There are now a lot of new comments
### Removed
- We removed an unnecessary `if` statement
### Fixed
- The `isWin`, and `line: 250` `try-except` now has an exception type
- We found (and fixed) a lot of not `error()` error messages

## [1.1.2] - 2021-04-10
### Removed
- Removed some unused variables (`i`s in for loops)
### Fixed
- We now use (for testing `False` and `None`) `is` (`PTC-W0068`)

## [1.1.1] - 2021-03-25
### Added
- Now the functions have documention.
### Fixed
- Fixed the `Unnecessary "else" after "return"` issues ([#8](https://github.com/koviubi56/cardjitsu/issues/8) [#9](https://github.com/koviubi56/cardjitsu/issues/9))
- Fixed the `Using type() instead of isinstance() for a typecheck.` issue ([#7](https://github.com/koviubi56/cardjitsu/issues/7)).

## [1.1.0] - 2021-03-22
### Changed
- A lot of changed happend to make the code better (e.g. write code once)

## [1.0.0] - 2021-03-20
### Added
- Now you can play with, and without colors
### Changed
- Unnecessary import deleted
### Fixed
- If you lose, you don't get your winned cards

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
- If there is an if commands, now we specife every condition, also the last condition too (https://is.gd/k56_cardjitsu_1)
- Now the userChoice variable is `{"type": userT, "level": userL, "color": userC}`, and we use the variable, and not write that long string
- Now you have 10 cards
### Removed
- The version print at the start of the code (`if __name__ == '__main__':`)
### Fixed
- The level of a card now can't be 0 (*replaced 0 with 1*)
- Now the used cards will be displayed (not just the water)
- Now you can see your winned snow cards (*replaced 2 with 3*)

## [1.0.0-alpha.1] - 2021-03-15
