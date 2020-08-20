# AutoTestTables


[![Build Status](https://travis-ci.com/Skelmis/autotesttables.svg?branch=master)](https://travis-ci.com/Skelmis/autotesttables)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AutoTestTables is Python package made to further automate testing, by automatically generating test tables.

# New Features!

  - Save test tables to an excel document or print to stdout

## Table of Contents


- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Team](#team)
- [License](#license)


---

### Installation

AutoTestTables requires [Python3+](https://www.python.org/) to run.
> It has been tested on 3.7 & 3.8, other versions are unsupported.


```

$ pip install autotesttables
```

----

### Usage

The simplest implementation of this works with all of the defaults and can be called with two lines.
Create a new file in the directory of your tests and put the following, this will use the defaults and print output to stdout.
```

from autotesttables import TestProgram

if __name__ == "__main__":
    TestProgram(module=None)

```

For a more comprehensive usage where we wish to change some values we will use `TestProgram` to create Generator instance and change the relevant settings. This example shows how to change the program to save to a excel document with the default name
```python
This feature is still a work in progress

<https://github.com/Skelmis/autotesttables/blob/master/autotesttables/generator.py#L274>

manipulate this to force output differently.
```

----

### Contributing

Please open either an [Issue](https://github.com/Skelmis/autotesttables/issues) or [Pull Request](https://github.com/Skelmis/autotesttables/pulls) stating your changes / discovered issues / wanted enhancements

----


### Team
Lead Developer - [Ethan](https://github.com/Skelmis)

----

### License

The MIT License (MIT)

Copyright (c) 2020 Ethan | Skelmis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
