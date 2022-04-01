# Linux-kernel-optimisation

Collection of scripts used to reconfigure and benchmark a linux system in web app performance.

Main components are:

1) Python scripts to change configuration files, track changes and save results.
2) Bash scripts to recopile the kernel, perform benchmarks and automatically run the process.


Sets of 32 tests are performed per configuration. The benchmark script itself contains the logic for result parsing and can be called separately, in which case command line parameters can be used to set the number of tests, reqest number, parallel connections.

JSON files are used to store configuration options, including the parameter name, type, range, current value and default value, as well as mutually exclusive parameters in some cases. With slight modifications boolean parameters could also be read from the machine's ".config file" directly.
