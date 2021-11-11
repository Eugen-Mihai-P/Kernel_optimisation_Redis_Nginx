- General setup
    - Compression mode
    - Enable process_vm_readv/writev syscalls
    - Timers subsystem
        - Timer tick handling
        - High Resolution Timer Support
    - RCU Subsystems
        -  (basically each option under RCU looks interesting)
    - Memory placement aware NUMA scheduler
        - Automatically enable NUMA aware memory/task placement
    - Automatic process group scheduling
    - Optimize for size
    - Configure standard kernel features (expert users)
        - Enable support for printk
        - Enable full-sized data structures for core
        - Enable futex support
        - Enable eventpoll support
        - Enable AIO support
        - Enable madvise/fadvise syscalls
    - Choose SLAB allocator
    - SLUB per-cpu partial caches
    - Optimize very unlikely/likely branches
    - Stack protector buffer overflow protection


- Enable the block layer
    - IO Schedulers
        - Default I/O scheduler


- Processor type and features
    - Single depth WCHAN output
    - Processor family
    - SMT (Hyperthreading) scheduler support
    - Preemption model
    - Enable 1GB pages for kernel pagetables
    - NUMA memory allocation and scheduler support
    - Sparse memory virtual memory map
    - Transparent hugepages support
    - Supervisor mode access prevention
    - Timer frequency


- Power management and ACPI options
    - Enable workqueue power-efficient mode by default
    - CPU frequency scaling
        - Default CPUFreq governor
    - CPU frequency translation statistics
    - Suspend to RAM and standby
        - Hybernation
        - Opportunistic sleep

(Let's scope out drivers, network and filesystems for now. For network and
filesystem I assume most options can be changed at runtime)

- Kernel Hacking
    - Set upper limit of TLB entries to flush one-by-one
