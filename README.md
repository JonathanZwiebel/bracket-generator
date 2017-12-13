# bracket-generator
A set of small scripts to generate and run standard-format brackets in python

These scripts are meant to generate simple tournament brackets.

# Supported Game Types:
Currently only head-to-head win/loss single play single outcome games are playable. 

Content to add for games include:
 - Three of more player games
 - Support for tied games
 - Support for canceled games
 - Score reporting for games (for eventual use in tiebreaking scenarios)
 - Support for games with variable outcomes (ex. Knockout vs Decision vs Disqualification)
 - Support for best of N series games

# Supported Bracket Types
Currently only single elimination brackets with sequential or random seeding are supported. 

Content to add for brackets include:
 - N-ple elimination standard brackets
 - Swiss style brackets
 - Round robin and split round robin style brackets
 - Gauntlet style brackets
 - Multistage brackets (i.e. round robin group stage to lead into single elimination bracket)
 - Determination of Nth place positions
 - Bucket based seeding


# Output:
Currently all output is done on the command line and with minimal functionality

To add for output:
 - Standalone GUI display (tkinder)
 - Web app display 
 - Mobile application display
 - Printable display
 - Shareable display
 - Notification posting to social media / Slack 

# Other Functionality:
 - Verification on winner and game IDs
 - Listing of legal games to be played in a given round
 
 To Add:
  - Game scheduling
  - Post-game results modification
  - Tournament drop out status
  - Player based statistics
  - Post-tournament analysis and results summary
