from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform


_io = [
    ("user_led", 0, Pins("AG9"), IOStandard("LVCMOS33")),  # sfp1_led1
    ("user_led", 1, Pins("AJ10"), IOStandard("LVCMOS33")), # sfp1_led2
    ("user_led", 2, Pins("AJ13"), IOStandard("LVCMOS33")), # sfp2_led1
    ("user_led", 3, Pins("AE13"), IOStandard("LVCMOS33")), # sfp2_led2

    ("clk50", 0, Pins("AF9"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("AK8")),
        Subsignal("rx", Pins("AL8")),
        IOStandard("LVCMOS33")
    ),
    ("serial", 1,
        Subsignal("tx", Pins("M27")),
        Subsignal("rx", Pins("L27")),
        IOStandard("LVCMOS33")
    ),
    ("serial_rtm", 0,
        Subsignal("tx", Pins("G27")),
        Subsignal("rx", Pins("H27")),
        IOStandard("LVCMOS33")
    ),

    # this is the second SPI flash (not containing the bitstream)
    # clock is shared with the bitstream flash and needs to be accessed
    # through STARTUPE3
    ("spiflash", 0,
        Subsignal("cs_n", Pins("K21")),
        Subsignal("dq", Pins("M20 L20 R21 R22")),
        IOStandard("LVCMOS33")
    ),

    ("ddram_32", 1,
        Subsignal("a", Pins(
            "E15 D15 J16 K18 H16 K17 K16 J15",
            "K15 D14 D18 G15 L18 G14 L15"),
            IOStandard("SSTL15")),
        Subsignal("ba", Pins("L19 H17 G16"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("E18"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("E16"), IOStandard("SSTL15")),
        Subsignal("we_n", Pins("D16"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("G19"), IOStandard("SSTL15")),
        Subsignal("dm", Pins("F27 E26 D23 G24"),
            IOStandard("SSTL15"),
            Misc("DATA_RATE=DDR")),
        Subsignal("dq", Pins(
            "C28 B27 A27 C27 D28 E28 A28 D29",
            "D25 C26 E25 B25 C24 A25 D24 B26",
            "B20 D21 B22 E23 E22 D20 B21 A20",
            "F23 H21 F24 G21 F22 E21 G22 E20"),
            IOStandard("SSTL15_DCI"),
            Misc("ODT=RTT_40"),
            Misc("DATA_RATE=DDR")),
        Subsignal("dqs_p", Pins("B29 B24 C21 G20"),
            IOStandard("DIFF_SSTL15"),
            Misc("DATA_RATE=DDR")),
        Subsignal("dqs_n", Pins("A29 A24 C22 F20"),
            IOStandard("DIFF_SSTL15"),
            Misc("DATA_RATE=DDR")),
        Subsignal("clk_p", Pins("J19"), IOStandard("DIFF_SSTL15"), Misc("DATA_RATE=DDR")),
        Subsignal("clk_n", Pins("J18"), IOStandard("DIFF_SSTL15"), Misc("DATA_RATE=DDR")),
        Subsignal("cke", Pins("H18"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("F19"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("F14"), IOStandard("LVCMOS15")),
        Misc("SLEW=FAST"),
    ),

    ("ddram_64", 0,
        Subsignal("a", Pins(
            "AE17 AL17 AG16 AG17 AD16 AH14 AD15 AK15",
            "AF14 AF15 AL18 AL15 AE18 AJ15 AG14"),
            IOStandard("SSTL15")),
        Subsignal("ba", Pins("AF17 AD19 AD18"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("AH19"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("AK18"), IOStandard("SSTL15")),
        Subsignal("we_n", Pins("AG19"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("AF18"), IOStandard("SSTL15")),
        Subsignal("dm", Pins("AD21 AE25 AJ21 AM21 AH26 AN26 AJ29 AL32"),
            IOStandard("SSTL15"),
            Misc("DATA_RATE=DDR")),
        Subsignal("dq", Pins(
            "AE23 AG20 AF22 AF20 AE22 AD20 AG22 AE20",
            "AJ24 AG24 AJ23 AF23 AH23 AF24 AH22 AG25",
            "AL22 AL25 AM20 AK23 AK22 AL24 AL20 AL23",
            "AM24 AN23 AN24 AP23 AP25 AN22 AP24 AM22",
            "AH28 AK26 AK28 AM27 AJ28 AH27 AK27 AM26",
            "AL30 AP29 AM30 AN28 AL29 AP28 AM29 AN27",
            "AH31 AH32 AJ34 AK31 AJ31 AJ30 AH34 AK32",
            "AN33 AP33 AM34 AP31 AM32 AN31 AL34 AN32"),
            IOStandard("SSTL15_DCI"),
            Misc("ODT=RTT_40"),
            Misc("DATA_RATE=DDR")),
        Subsignal("dqs_p", Pins("AG21 AH24 AJ20 AP20 AL27 AN29 AH33 AN34"),
            IOStandard("DIFF_SSTL15"),
            Misc("DATA_RATE=DDR")),
        Subsignal("dqs_n", Pins("AH21 AJ25 AK20 AP21 AL28 AP30 AJ33 AP34"),
            IOStandard("DIFF_SSTL15"),
            Misc("DATA_RATE=DDR")),
        Subsignal("clk_p", Pins("AE16"), IOStandard("DIFF_SSTL15"), Misc("DATA_RATE=DDR")),
        Subsignal("clk_n", Pins("AE15"), IOStandard("DIFF_SSTL15"), Misc("DATA_RATE=DDR")),
        Subsignal("cke", Pins("AL19"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("AJ18"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("AJ14"), IOStandard("LVCMOS15")),
        Misc("SLEW=FAST"),
    ),

    ("eth_clocks", 0,
        Subsignal("tx", Pins("M22")),
        Subsignal("rx", Pins("T25")),
        IOStandard("LVCMOS33")
    ),
    ("eth", 0,
        Subsignal("rx_ctl", Pins("T24")),
        Subsignal("rx_data", Pins("R23 P23 R25 R26")),
        Subsignal("tx_ctl", Pins("N22")),
        Subsignal("tx_data", Pins("K20 K22 P20 P21")),
        Subsignal("mdc", Pins("T27")),
        Subsignal("mdio", Pins("R27")),
        IOStandard("LVCMOS33")
    ),

    ("sma_io", 0,
        Subsignal("level", Pins("K23")),
        Subsignal("direction", Pins("K25")),
        IOStandard("LVCMOS33")
    ),
    ("sma_io", 1,
        Subsignal("level", Pins("L25")),
        Subsignal("direction", Pins("L23")),
        IOStandard("LVCMOS33")
    ),

    ("amc_rtm_serwb", 0,
        Subsignal("clk_p", Pins("J8")), # rtm_fpga_usr_io_p
        Subsignal("clk_n", Pins("H8")), # rtm_fpga_usr_io_n
        Subsignal("tx_p", Pins("A13")), # rtm_fpga_lvds1_p
        Subsignal("tx_n", Pins("A12")), # rtm_fpga_lvds1_n
        Subsignal("rx_p", Pins("C12")), # rtm_fpga_lvds2_p
        Subsignal("rx_n", Pins("B12")), # rtm_fpga_lvds2_n
        IOStandard("LVDS")
    ),
]


_connectors = [
    ("LPC", {
        "LA33_N": "V28",
        "LA32_N": "U25",
        "LA31_N": "Y28",
        "LA30_N": "U27",
        "LA29_N": "W29",
        "LA28_N": "W26",
        "LA27_N": "AB26",
        "LA26_N": "AB22",
        "LA25_N": "AB20",
        "LA24_N": "AC23",
        "LA23_N": "AC21",
        "LA22_N": "U22",
        "LA21_N": "W21",
        "LA20_N": "T23",
        "LA19_N": "V23",
        "LA18_CC_N": "Y25",
        "LA17_CC_N": "W24",
        "LA16_N": "Y30",
        "LA15_N": "Y32",
        "LA14_N": "V34",
        "LA13_N": "Y33",
        "LA12_N": "W31",
        "LA11_N": "AB29",
        "LA10_N": "AB34",
        "LA09_N": "AF32",
        "LA08_N": "AD31",
        "LA07_N": "AD33",
        "LA06_N": "AD34",
        "LA05_N": "AF34",
        "LA04_N": "AG32",
        "LA03_N": "W34",
        "LA02_N": "AG34",
        "LA01_CC_N": "AB31",
        "LA00_CC_N": "AB32",
        "LA33_P": "V27",
        "LA32_P": "U24",
        "LA31_P": "W28",
        "LA30_P": "U26",
        "LA29_P": "V29",
        "LA28_P": "V26",
        "LA27_P": "AB25",
        "LA26_P": "AA22",
        "LA25_P": "AA20",
        "LA24_P": "AC22",
        "LA23_P": "AB21",
        "LA22_P": "U21",
        "LA21_P": "V21",
        "LA20_P": "T22",
        "LA19_P": "V22",
        "LA18_CC_P": "W25",
        "LA17_CC_P": "W23",
        "LA16_P": "W30",
        "LA15_P": "Y31",
        "LA14_P": "U34",
        "LA13_P": "W33",
        "LA12_P": "V31",
        "LA11_P": "AA29",
        "LA10_P": "AA34",
        "LA09_P": "AE32",
        "LA08_P": "AD30",
        "LA07_P": "AC33",
        "LA06_P": "AC34",
        "LA05_P": "AE33",
        "LA04_P": "AG31",
        "LA03_P": "V33",
        "LA02_P": "AF33",
        "LA01_CC_P": "AB30",
        "LA00_CC_P": "AA32",
        # LVDS
        "CLK0_M2C_N": "AA25",
        "CLK0_M2C_P": "AA24",
        "CLK1_M2C_N": "AA23",
        "CLK1_M2C_P": "Y23",
        # DIFF_HSTL_I_DCI_18
        "GBTCLK0_M2C_P": "AC31",
        "GBTCLK0_M2C_N": "AC32",
        "DP0_M2C_P": "AE27",
        "DP0_M2C_N": "AF27",
        "DP0_C2M_P": "AE28",
        "DP0_C2M_N": "AF28",
    }),
]


class Platform(XilinxPlatform):
    default_clk_name = "clk50"
    default_clk_period = 20.0

    def __init__(self):
        XilinxPlatform.__init__(
                self, "xcku040-ffva1156-1-c", _io, _connectors,
                toolchain="vivado")

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        try:
            self.add_period_constraint(
                    self.lookup_request("eth_clocks").rx, 8.0)
        except ConstraintError:
            pass
        try:
            self.add_period_constraint(
                    self.lookup_request("eth_clocks").tx, 8.0)
        except ConstraintError:
            pass
