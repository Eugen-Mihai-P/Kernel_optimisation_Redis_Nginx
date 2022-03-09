- General setup
    - Compression mode						# CONFIG_KERNEL_compType
    
    - Preemption model						# CONFIG_PREEMPT_VOLUNTARY/ CONFIG_PREEMPT_NONE/ CONFIG_PREEMPT + CONFIG_PREEMPT_DYNAMIC
    
    - Enable process_vm_readv/writev syscalls			# CONFIG_CROSS_MEMORY_ATTACH
    
    - Timers subsystem						
        - Timer tick handling					# CONFIG_NO_HZ_IDLE/CONFIG_NO_HZ_FULL/ CONFIG_HZ_PERIODIC
        - High Resolution Timer Support				# CONFIG_HIGH_RES_TIMERS
    
    - RCU Subsystems
        -  (basically each option under RCU looks interesting)
							# CONFIG_RCU_EXPERT: y
								# CONFIG_RCU_FANOUT: integer [2 64]
								# CONFIG_RCU_FANOUT_LEAF [2 64]
								# CONFIG_RCU_FAST_NO_HZ : boolean
								# CONFIG_RCU_BOOST: boolean
								# CONFIG_RCU_NOCB_CPU: boolean
        	
        
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
    - SLUB per-cpu partial caches				# CONFIG_SLUB_CPU_PARTIAL
    - Optimize very unlikely/likely branches			# CONFIG_SLUB/SLAB/SLOB
    - Stack protector buffer overflow protection


- Enable the block layer
    - IO Schedulers
        - Default I/O scheduler


- Processor type and features
    - Single depth WCHAN output					CONFIG_SCHED_OMIT_FRAME_POINTER
    - Processor family						# 
    - SMT (Hyperthreading) scheduler support  			# CONFIG_SCHED_SMT
    - Preemption model						# 
    - Enable 1GB pages for kernel pagetables
    - NUMA memory allocation and scheduler support		# CONFIG_NUMA
    - Sparse memory virtual memory map				
    - Transparent hugepages support
    - Supervisor mode access prevention 			# 
    - Timer frequency						# CONFIG_HZ_xxx


- Power management and ACPI options
    - Enable workqueue power-efficient mode by default		# 
    - CPU frequency scaling
        - Default CPUFreq governor			# CONFIG_CPU_FREQ_DEFAULT_GOV_SCHEDUTIL/ userspace/ powersave/ performance (alternatively without default)
    - CPU frequency translation statistics
    - Suspend to RAM and standby
        - Hybernation
        - Opportunistic sleep

(Let's scope out drivers, network and filesystems for now. For network and
filesystem I assume most options can be changed at runtime)

- Kernel Hacking
    - Set upper limit of TLB entries to flush one-by-one
    
    
    
    
    
    
# CONFIG_SCHED_CORE
