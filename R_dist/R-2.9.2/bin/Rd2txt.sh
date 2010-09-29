##
## Rd2txt -- Convert man pages (*.Rd help files) to plain text.

revision='$Rev: 47589 $'
version=`set - ${revision}; echo ${2}`
version="Rd2txt: ${R_VERSION} (r${version})

Copyright (C) 2000 The R Core Development Team.
This is free software; see the GNU General Public License version 2
or later for copying conditions.  There is NO warranty."

usage="Usage: R CMD Rd2txt [options] file

Generate plain text output from the Rd source specified by file.

Options:
  -h, --help		print short help message and exit
  -v, --version		print version info and exit  

Report bugs to <r-bugs@r-project.org>."  

case "${1}" in
  -h|--help)
    echo "${usage}"; exit 0 ;;
  -v|--version)
    echo "${version}"; exit 0 ;;
esac

perl ${R_HOME}/bin/Rdconv -t txt "${1}"

### Local Variables: ***
### mode: sh ***
### sh-indentation: 2 ***
### End: ***
