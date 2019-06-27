# Timing-Summary-Fucker

a Python script that modify Vivado timing summaries to pass plagiarism detection.

---

## Usage
```
$ python fuck_summary.py --help
usage: fuck_summary.py [-h] [-o OUTPUT] [-m MIN_SCALE] [-M MAX_SCALE]
                       [--mean MEAN] [--std STD]
                       path

Fuck up your Vivado timing summary

positional arguments:
  path                  original timing summary path

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output path
  -m MIN_SCALE, --min-scale MIN_SCALE
                        min zoom scale
  -M MAX_SCALE, --max-scale MAX_SCALE
                        max zoom scale
  --mean MEAN           mean of zoom scale
  --std STD             standard deviation of zoom scale
```

## Demo
```
$ cat example_summary.txt
Slack (MET) :             98.115ns  (required time - arrival time)
  Source:                 div/clk_reg/C
                            (rising edge-triggered cell FDRE clocked by clk_pin  {rise@0.000ns fall@50.000ns period=100.000ns})
  Destination:            div/clk_reg/D
                            (rising edge-triggered cell FDRE clocked by clk_pin  {rise@0.000ns fall@50.000ns period=100.000ns})
  Path Group:             clk_pin
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            100.000ns  (clk_pin rise@100.000ns - clk_pin rise@0.000ns)
  Data Path Delay:        1.749ns  (logic 0.773ns (44.197%)  route 0.976ns (55.803%))
  Logic Levels:           1  (LUT6=1)
  Clock Path Skew:        -0.145ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    2.704ns = ( 102.704 - 100.000 )
    Source Clock Delay      (SCD):    2.965ns
    Clock Pessimism Removal (CPR):    0.116ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk_pin rise edge)    0.000     0.000 r
    E3                                                0.000     0.000 r  clk_in (IN)
                         net (fo=0)                   0.000     0.000    clk_in
    E3                                                                r  clk_in_IBUF_inst/I
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk_in_IBUF_inst/O

  -------------------------------------------------------------------    -------------------
                         FDRE (Prop_fdre_C_Q)         0.478     3.443 r  div/clk_reg/Q
                         net (fo=2, unplaced)         0.976     4.419    div/clk
                                                                      r  div/clk_i_1/I0
                         LUT6 (Prop_lut6_I0_O)        0.295     4.714 r  div/clk_i_1/O
```

```
$ python fuck_summary.py example_summary.txt -o new_summary.txt
```

```
$ cat new_summary.txt
Slack (MET) :             73.586ns  (required time - arrival time)
  Source:                 div/clk_reg/C
                            (rising edge-triggered cell FDRE clocked by clk_pin  {rise@0.000ns fall@62.500ns period=75.000ns})
  Destination:            div/clk_reg/D
                            (rising edge-triggered cell FDRE clocked by clk_pin  {rise@0.000ns fall@62.500ns period=125.000ns})
  Path Group:             clk_pin
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            125.000ns  (clk_pin rise@125.000ns - clk_pin rise@0.000ns)
  Data Path Delay:        2.186ns  (logic 0.609ns (33.148%)  route 1.220ns (69.754%))
  Logic Levels:           1  (LUT6=1)
  Clock Path Skew:        -0.109ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    3.054ns = ( 103.054 - 125.000 )
    Source Clock Delay      (SCD):    3.706ns
    Clock Pessimism Removal (CPR):    0.087ns
  Clock Uncertainty:      0.044ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.089ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk_pin rise edge)    0.000     0.000 r
    E3                                                0.000     0.000 r  clk_in (IN)
                         net (fo=0)                   0.000     0.000    clk_in
    E3                                                                r  clk_in_IBUF_inst/I
    E3                   IBUF (Prop_ibuf_I_O)         1.853     1.853 r  clk_in_IBUF_inst/O

  -------------------------------------------------------------------    -------------------
                         FDRE (Prop_fdre_C_Q)         0.597     4.304 r  div/clk_reg/Q
                         net (fo=2, unplaced)         1.220     3.967    div/clk
                                                                      r  div/clk_i_1/I0
                         LUT6 (Prop_lut6_I0_O)        0.323     5.893 r  div/clk_i_1/O
```

## TODO
- [x] modify numbers
- [ ] modify path names
- [x] add cmd argument parser