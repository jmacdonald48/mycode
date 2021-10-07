#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons


def main():
    """run time code. Always indent under function"""

    # print 'red string' in red
    print(crayons.white('Jack'),crayons.green('Mac'))



# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

