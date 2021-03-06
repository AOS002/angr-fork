###
### This file was automatically generated
###

from archinfo.arch import register_arch, Endness, Register

from .common import ArchPcode


class ArchPcode_AARCH64_LE_64_v8A(ArchPcode):
    name = 'AARCH64:LE:64:v8A'
    pcode_arch = 'AARCH64:LE:64:v8A'
    description = 'Generic ARM v8.5-A LE instructions, LE data, missing some 8.5 vector'
    bits = 64
    ip_offset = 0x0
    sp_offset = 0x8
    bp_offset = sp_offset
    instruction_endness = Endness.LE
    register_list = [
        Register('pc', 8, 0x0, alias_names=('ip',)),
        Register('sp', 8, 0x8),
        Register('wsp', 4, 0x8),
        Register('ng', 1, 0x100),
        Register('zr', 1, 0x101),
        Register('cy', 1, 0x102),
        Register('ov', 1, 0x103),
        Register('shift_carry', 1, 0x104),
        Register('tmpcy', 1, 0x105),
        Register('tmpov', 1, 0x106),
        Register('tmpng', 1, 0x107),
        Register('tmpzr', 1, 0x108),
        Register('glob_mask32', 4, 0x200),
        Register('glob_mask64', 8, 0x204),
        Register('vecmemaddr', 8, 0x300),
        Register('vectorselem', 8, 0x308),
        Register('vecregaddr', 4, 0x310),
        Register('spsr_el1', 8, 0x1000),
        Register('elr_el1', 8, 0x1008),
        Register('sp_el0', 8, 0x1010),
        Register('spsel', 8, 0x1018),
        Register('daif', 8, 0x1020),
        Register('currentel', 8, 0x1028),
        Register('nzcv', 8, 0x1030),
        Register('fpcr', 8, 0x1038),
        Register('fpsr', 8, 0x1040),
        Register('dspsr_el0', 8, 0x1048),
        Register('dlr_el0', 8, 0x1050),
        Register('spsr_el2', 8, 0x1058),
        Register('elr_el2', 8, 0x1060),
        Register('sp_el1', 8, 0x1068),
        Register('spsr_irq', 8, 0x1070),
        Register('spsr_abt', 8, 0x1078),
        Register('spsr_und', 8, 0x1080),
        Register('spsr_fiq', 8, 0x1088),
        Register('spsr_el3', 8, 0x1090),
        Register('elr_el3', 8, 0x1098),
        Register('sp_el2', 8, 0x10a0),
        Register('spsr_svc', 8, 0x10a8),
        Register('spsr_hyp', 8, 0x10b0),
        Register('uao', 8, 0x10b8),
        Register('pan', 8, 0x10c0),
        Register('tco', 8, 0x10c8),
        Register('midr_el1', 8, 0x1100),
        Register('mpidr_el1', 8, 0x1108),
        Register('revidr_el1', 8, 0x1110),
        Register('id_dfr0_el1', 8, 0x1118),
        Register('id_pfr0_el1', 8, 0x1120),
        Register('id_pfr1_el1', 8, 0x1128),
        Register('id_afr0_el1', 8, 0x1130),
        Register('id_mmfr0_el1', 8, 0x1138),
        Register('id_mmfr1_el1', 8, 0x1140),
        Register('id_mmfr2_el1', 8, 0x1148),
        Register('id_mmfr3_el1', 8, 0x1150),
        Register('id_isar0_el1', 8, 0x1158),
        Register('id_isar1_el1', 8, 0x1160),
        Register('id_isar2_el1', 8, 0x1168),
        Register('id_isar3_el1', 8, 0x1170),
        Register('id_isar4_el1', 8, 0x1178),
        Register('id_isar5_el1', 8, 0x1180),
        Register('mvfr0_el1', 8, 0x1188),
        Register('mvfr1_el1', 8, 0x1190),
        Register('mvfr2_el1', 8, 0x1198),
        Register('ccsidr_el1', 8, 0x11a0),
        Register('id_aa64pfr0_el1', 8, 0x11a8),
        Register('id_aa64pfr1_el1', 8, 0x11b0),
        Register('id_aa64dfr0_el1', 8, 0x11b8),
        Register('id_aa64dfr1_el1', 8, 0x11c0),
        Register('id_aa64isar0_el1', 8, 0x11c8),
        Register('id_aa64isar1_el1', 8, 0x11d0),
        Register('id_aa64mmfr0_el1', 8, 0x11d8),
        Register('id_aa64mmfr1_el1', 8, 0x11e0),
        Register('id_aa64afr0_el1', 8, 0x11e8),
        Register('id_aa64afr1_el1', 8, 0x11f0),
        Register('clidr_el1', 8, 0x11f8),
        Register('aidr_el1', 8, 0x1200),
        Register('csselr_el1', 8, 0x1208),
        Register('ctr_el0', 8, 0x1210),
        Register('dczid_el0', 8, 0x1218),
        Register('vpidr_el2', 8, 0x1220),
        Register('vmpidr_el2', 8, 0x1228),
        Register('sctlr_el1', 8, 0x1230),
        Register('actlr_el1', 8, 0x1238),
        Register('cpacr_el1', 8, 0x1240),
        Register('sctlr_el2', 8, 0x1248),
        Register('actlr_el2', 8, 0x1250),
        Register('hcr_el2', 8, 0x1258),
        Register('mdcr_el2', 8, 0x1260),
        Register('cptr_el2', 8, 0x1268),
        Register('hstr_el2', 8, 0x1270),
        Register('hacr_el2', 8, 0x1278),
        Register('sctlr_el3', 8, 0x1280),
        Register('actlr_el3', 8, 0x1288),
        Register('scr_el3', 8, 0x1290),
        Register('cptr_el3', 8, 0x1298),
        Register('mdcr_el3', 8, 0x12a0),
        Register('ttbr0_el1', 8, 0x12a8),
        Register('ttbr1_el1', 8, 0x12b0),
        Register('ttbr0_el2', 8, 0x12b8),
        Register('ttbr0_el3', 8, 0x12c0),
        Register('vttbr_el2', 8, 0x12c8),
        Register('tcr_el1', 8, 0x12d0),
        Register('tcr_el2', 8, 0x12d8),
        Register('tcr_el3', 8, 0x12e0),
        Register('vtcr_el2', 8, 0x12e8),
        Register('afsr0_el1', 8, 0x12f0),
        Register('afsr1_el1', 8, 0x12f8),
        Register('afsr0_el2', 8, 0x1300),
        Register('afsr1_el2', 8, 0x1308),
        Register('afsr0_el3', 8, 0x1310),
        Register('afsr1_el3', 8, 0x1318),
        Register('esr_el1', 8, 0x1320),
        Register('esr_el2', 8, 0x1328),
        Register('esr_el3', 8, 0x1330),
        Register('fpexc32_el2', 8, 0x1338),
        Register('far_el1', 8, 0x1340),
        Register('far_el2', 8, 0x1348),
        Register('far_el3', 8, 0x1350),
        Register('hpfar_el2', 8, 0x1358),
        Register('par_el1', 8, 0x1360),
        Register('pmintenset_el1', 8, 0x1368),
        Register('pmintenclr_el1', 8, 0x1370),
        Register('pmcr_el0', 8, 0x1378),
        Register('pmcntenset_el0', 8, 0x1380),
        Register('pmcntenclr_el0', 8, 0x1388),
        Register('pmovsclr_el0', 8, 0x1390),
        Register('pmswinc_el0', 8, 0x1398),
        Register('pmselr_el0', 8, 0x13a0),
        Register('pmceid0_el0', 8, 0x13a8),
        Register('pmceid1_el0', 8, 0x13b0),
        Register('pmccntr_el0', 8, 0x13b8),
        Register('pmxevtyper_el0', 8, 0x13c0),
        Register('pmxevcntr_el0', 8, 0x13c8),
        Register('pmuserenr_el0', 8, 0x13d0),
        Register('pmovsset_el0', 8, 0x13d8),
        Register('pmevcntr0_el0', 8, 0x13e0),
        Register('pmevcntr1_el0', 8, 0x13e8),
        Register('pmevcntr2_el0', 8, 0x13f0),
        Register('pmevcntr3_el0', 8, 0x13f8),
        Register('pmevcntr4_el0', 8, 0x1400),
        Register('pmevcntr5_el0', 8, 0x1408),
        Register('pmevcntr6_el0', 8, 0x1410),
        Register('pmevcntr7_el0', 8, 0x1418),
        Register('pmevcntr8_el0', 8, 0x1420),
        Register('pmevcntr9_el0', 8, 0x1428),
        Register('pmevcntr10_el0', 8, 0x1430),
        Register('pmevcntr11_el0', 8, 0x1438),
        Register('pmevcntr12_el0', 8, 0x1440),
        Register('pmevcntr13_el0', 8, 0x1448),
        Register('pmevcntr14_el0', 8, 0x1450),
        Register('pmevcntr15_el0', 8, 0x1458),
        Register('pmevcntr16_el0', 8, 0x1460),
        Register('pmevcntr17_el0', 8, 0x1468),
        Register('pmevcntr18_el0', 8, 0x1470),
        Register('pmevcntr19_el0', 8, 0x1478),
        Register('pmevcntr20_el0', 8, 0x1480),
        Register('pmevcntr21_el0', 8, 0x1488),
        Register('pmevcntr22_el0', 8, 0x1490),
        Register('pmevcntr23_el0', 8, 0x1498),
        Register('pmevcntr24_el0', 8, 0x14a0),
        Register('pmevcntr25_el0', 8, 0x14a8),
        Register('pmevcntr26_el0', 8, 0x14b0),
        Register('pmevcntr27_el0', 8, 0x14b8),
        Register('pmevcntr28_el0', 8, 0x14c0),
        Register('pmevcntr29_el0', 8, 0x14c8),
        Register('pmevcntr30_el0', 8, 0x14d0),
        Register('pmevtyper0_el0', 8, 0x14d8),
        Register('pmevtyper1_el0', 8, 0x14e0),
        Register('pmevtyper2_el0', 8, 0x14e8),
        Register('pmevtyper3_el0', 8, 0x14f0),
        Register('pmevtyper4_el0', 8, 0x14f8),
        Register('pmevtyper5_el0', 8, 0x1500),
        Register('pmevtyper6_el0', 8, 0x1508),
        Register('pmevtyper7_el0', 8, 0x1510),
        Register('pmevtyper8_el0', 8, 0x1518),
        Register('pmevtyper9_el0', 8, 0x1520),
        Register('pmevtyper10_el0', 8, 0x1528),
        Register('pmevtyper11_el0', 8, 0x1530),
        Register('pmevtyper12_el0', 8, 0x1538),
        Register('pmevtyper13_el0', 8, 0x1540),
        Register('pmevtyper14_el0', 8, 0x1548),
        Register('pmevtyper15_el0', 8, 0x1550),
        Register('pmevtyper16_el0', 8, 0x1558),
        Register('pmevtyper17_el0', 8, 0x1560),
        Register('pmevtyper18_el0', 8, 0x1568),
        Register('pmevtyper19_el0', 8, 0x1570),
        Register('pmevtyper20_el0', 8, 0x1578),
        Register('pmevtyper21_el0', 8, 0x1580),
        Register('pmevtyper22_el0', 8, 0x1588),
        Register('pmevtyper23_el0', 8, 0x1590),
        Register('pmevtyper24_el0', 8, 0x1598),
        Register('pmevtyper25_el0', 8, 0x15a0),
        Register('pmevtyper26_el0', 8, 0x15a8),
        Register('pmevtyper27_el0', 8, 0x15b0),
        Register('pmevtyper28_el0', 8, 0x15b8),
        Register('pmevtyper29_el0', 8, 0x15c0),
        Register('pmevtyper30_el0', 8, 0x15c8),
        Register('pmccfiltr_el0', 8, 0x15d0),
        Register('mair_el1', 8, 0x15d8),
        Register('mair_el2', 8, 0x15e0),
        Register('mair_el3', 8, 0x15e8),
        Register('amair_el1', 8, 0x15f0),
        Register('amair_el2', 8, 0x15f8),
        Register('amair_el3', 8, 0x1600),
        Register('vbar_el1', 8, 0x1608),
        Register('vbar_el2', 8, 0x1610),
        Register('vbar_el3', 8, 0x1618),
        Register('rvbar_el1', 8, 0x1620),
        Register('rvbar_el2', 8, 0x1628),
        Register('rvbar_el3', 8, 0x1630),
        Register('rmr_el1', 8, 0x1638),
        Register('rmr_el2', 8, 0x1640),
        Register('rmr_el3', 8, 0x1648),
        Register('isr_el1', 8, 0x1650),
        Register('contextidr_el1', 8, 0x1658),
        Register('tpidr_el0', 8, 0x1660),
        Register('tpidrro_el0', 8, 0x1668),
        Register('tpidr_el1', 8, 0x1670),
        Register('tpidr_el2', 8, 0x1678),
        Register('tpidr_el3', 8, 0x1680),
        Register('teecr32_el1', 8, 0x1688),
        Register('cntfrq_el0', 8, 0x1690),
        Register('cntpct_el0', 8, 0x1698),
        Register('cntvct_el0', 8, 0x16a0),
        Register('cntvoff_el2', 8, 0x16a8),
        Register('cntkctl_el1', 8, 0x16b0),
        Register('cnthctl_el2', 8, 0x16b8),
        Register('cntp_tval_el0', 8, 0x16c0),
        Register('cntp_ctl_el0', 8, 0x16c8),
        Register('cntp_cval_el0', 8, 0x16d0),
        Register('cntv_tval_el0', 8, 0x16d8),
        Register('cntv_ctl_el0', 8, 0x16e0),
        Register('cntv_cval_el0', 8, 0x16e8),
        Register('cnthp_tval_el2', 8, 0x16f0),
        Register('cnthp_ctl_el2', 8, 0x16f8),
        Register('cnthp_cval_el2', 8, 0x1700),
        Register('cntps_tval_el1', 8, 0x1708),
        Register('cntps_ctl_el1', 8, 0x1710),
        Register('cntps_cval_el1', 8, 0x1718),
        Register('dacr32_el2', 8, 0x1720),
        Register('ifsr32_el2', 8, 0x1728),
        Register('teehbr32_el1', 8, 0x1730),
        Register('sder32_el3', 8, 0x1738),
        Register('gmid_el1', 8, 0x1740),
        Register('gcr_el1', 8, 0x1748),
        Register('gcr_el1.exclude', 2, 0x1748),
        Register('ssbs', 8, 0x1750),
        Register('osdtrrx_el1', 8, 0x1800),
        Register('mdccint_el1', 8, 0x1808),
        Register('mdscr_el1', 8, 0x1810),
        Register('osdtrtx_el1', 8, 0x1818),
        Register('oseccr_el1', 8, 0x1820),
        Register('dbgbvr0_el1', 8, 0x1828),
        Register('dbgbvr1_el1', 8, 0x1830),
        Register('dbgbvr2_el1', 8, 0x1838),
        Register('dbgbvr3_el1', 8, 0x1840),
        Register('dbgbvr4_el1', 8, 0x1848),
        Register('dbgbvr5_el1', 8, 0x1850),
        Register('dbgbvr6_el1', 8, 0x1858),
        Register('dbgbvr7_el1', 8, 0x1860),
        Register('dbgbvr8_el1', 8, 0x1868),
        Register('dbgbvr9_el1', 8, 0x1870),
        Register('dbgbvr10_el1', 8, 0x1878),
        Register('dbgbvr11_el1', 8, 0x1880),
        Register('dbgbvr12_el1', 8, 0x1888),
        Register('dbgbvr13_el1', 8, 0x1890),
        Register('dbgbvr14_el1', 8, 0x1898),
        Register('dbgbvr15_el1', 8, 0x18a0),
        Register('dbgbcr0_el1', 8, 0x18a8),
        Register('dbgbcr1_el1', 8, 0x18b0),
        Register('dbgbcr2_el1', 8, 0x18b8),
        Register('dbgbcr3_el1', 8, 0x18c0),
        Register('dbgbcr4_el1', 8, 0x18c8),
        Register('dbgbcr5_el1', 8, 0x18d0),
        Register('dbgbcr6_el1', 8, 0x18d8),
        Register('dbgbcr7_el1', 8, 0x18e0),
        Register('dbgbcr8_el1', 8, 0x18e8),
        Register('dbgbcr9_el1', 8, 0x18f0),
        Register('dbgbcr10_el1', 8, 0x18f8),
        Register('dbgbcr11_el1', 8, 0x1900),
        Register('dbgbcr12_el1', 8, 0x1908),
        Register('dbgbcr13_el1', 8, 0x1910),
        Register('dbgbcr14_el1', 8, 0x1918),
        Register('dbgbcr15_el1', 8, 0x1920),
        Register('dbgwvr0_el1', 8, 0x1928),
        Register('dbgwvr1_el1', 8, 0x1930),
        Register('dbgwvr2_el1', 8, 0x1938),
        Register('dbgwvr3_el1', 8, 0x1940),
        Register('dbgwvr4_el1', 8, 0x1948),
        Register('dbgwvr5_el1', 8, 0x1950),
        Register('dbgwvr6_el1', 8, 0x1958),
        Register('dbgwvr7_el1', 8, 0x1960),
        Register('dbgwvr8_el1', 8, 0x1968),
        Register('dbgwvr9_el1', 8, 0x1970),
        Register('dbgwvr10_el1', 8, 0x1978),
        Register('dbgwvr11_el1', 8, 0x1980),
        Register('dbgwvr12_el1', 8, 0x1988),
        Register('dbgwvr13_el1', 8, 0x1990),
        Register('dbgwvr14_el1', 8, 0x1998),
        Register('dbgwvr15_el1', 8, 0x19a0),
        Register('dbgwcr0_el1', 8, 0x19a8),
        Register('dbgwcr1_el1', 8, 0x19b0),
        Register('dbgwcr2_el1', 8, 0x19b8),
        Register('dbgwcr3_el1', 8, 0x19c0),
        Register('dbgwcr4_el1', 8, 0x19c8),
        Register('dbgwcr5_el1', 8, 0x19d0),
        Register('dbgwcr6_el1', 8, 0x19d8),
        Register('dbgwcr7_el1', 8, 0x19e0),
        Register('dbgwcr8_el1', 8, 0x19e8),
        Register('dbgwcr9_el1', 8, 0x19f0),
        Register('dbgwcr10_el1', 8, 0x19f8),
        Register('dbgwcr11_el1', 8, 0x1a00),
        Register('dbgwcr12_el1', 8, 0x1a08),
        Register('dbgwcr13_el1', 8, 0x1a10),
        Register('dbgwcr14_el1', 8, 0x1a18),
        Register('dbgwcr15_el1', 8, 0x1a20),
        Register('mdrar_el1', 8, 0x1a28),
        Register('oslar_el1', 8, 0x1a30),
        Register('oslsr_el1', 8, 0x1a38),
        Register('osdlr_el1', 8, 0x1a40),
        Register('dbgprcr_el1', 8, 0x1a48),
        Register('dbgclaimset_el1', 8, 0x1a50),
        Register('dbgclaimclr_el1', 8, 0x1a58),
        Register('dbgauthstatus_el1', 8, 0x1a60),
        Register('mdccsr_el0', 8, 0x1a68),
        Register('dbgdtr_el0', 8, 0x1a70),
        Register('dbgdtrrx_el0', 8, 0x1a78),
        Register('dbgdtrtx_el0', 8, 0x1a80),
        Register('dbgvcr32_el2', 8, 0x1a88),
        Register('contextreg', 4, 0x3000),
        Register('tmp_ldwn', 4, 0x3100),
        Register('tmp_ldxn', 8, 0x3104),
        Register('tmp_stwn', 4, 0x310c),
        Register('tmp_stxn', 8, 0x3110),
        Register('x0', 8, 0x4000),
        Register('w0', 4, 0x4000),
        Register('x1', 8, 0x4008),
        Register('w1', 4, 0x4008),
        Register('x2', 8, 0x4010),
        Register('w2', 4, 0x4010),
        Register('x3', 8, 0x4018),
        Register('w3', 4, 0x4018),
        Register('x4', 8, 0x4020),
        Register('w4', 4, 0x4020),
        Register('x5', 8, 0x4028),
        Register('w5', 4, 0x4028),
        Register('x6', 8, 0x4030),
        Register('w6', 4, 0x4030),
        Register('x7', 8, 0x4038),
        Register('w7', 4, 0x4038),
        Register('x8', 8, 0x4040),
        Register('w8', 4, 0x4040),
        Register('x9', 8, 0x4048),
        Register('w9', 4, 0x4048),
        Register('x10', 8, 0x4050),
        Register('w10', 4, 0x4050),
        Register('x11', 8, 0x4058),
        Register('w11', 4, 0x4058),
        Register('x12', 8, 0x4060),
        Register('w12', 4, 0x4060),
        Register('x13', 8, 0x4068),
        Register('w13', 4, 0x4068),
        Register('x14', 8, 0x4070),
        Register('w14', 4, 0x4070),
        Register('x15', 8, 0x4078),
        Register('w15', 4, 0x4078),
        Register('x16', 8, 0x4080),
        Register('w16', 4, 0x4080),
        Register('x17', 8, 0x4088),
        Register('w17', 4, 0x4088),
        Register('x18', 8, 0x4090),
        Register('w18', 4, 0x4090),
        Register('x19', 8, 0x4098),
        Register('w19', 4, 0x4098),
        Register('x20', 8, 0x40a0),
        Register('w20', 4, 0x40a0),
        Register('x21', 8, 0x40a8),
        Register('w21', 4, 0x40a8),
        Register('x22', 8, 0x40b0),
        Register('w22', 4, 0x40b0),
        Register('x23', 8, 0x40b8),
        Register('w23', 4, 0x40b8),
        Register('x24', 8, 0x40c0),
        Register('w24', 4, 0x40c0),
        Register('x25', 8, 0x40c8),
        Register('w25', 4, 0x40c8),
        Register('x26', 8, 0x40d0),
        Register('w26', 4, 0x40d0),
        Register('x27', 8, 0x40d8),
        Register('w27', 4, 0x40d8),
        Register('x28', 8, 0x40e0),
        Register('w28', 4, 0x40e0),
        Register('x29', 8, 0x40e8),
        Register('w29', 4, 0x40e8),
        Register('x30', 8, 0x40f0),
        Register('w30', 4, 0x40f0),
        Register('xzr', 8, 0x40f8),
        Register('wzr', 4, 0x40f8),
        Register('tmpz1', 32, 0x4800),
        Register('tmpq1', 16, 0x4800),
        Register('tmpd1', 8, 0x4800),
        Register('tmps1', 4, 0x4800),
        Register('tmpz2', 32, 0x4820),
        Register('tmpq2', 16, 0x4820),
        Register('tmpd2', 8, 0x4820),
        Register('tmps2', 4, 0x4820),
        Register('tmpz3', 32, 0x4840),
        Register('tmpq3', 16, 0x4840),
        Register('tmpd3', 8, 0x4840),
        Register('tmps3', 4, 0x4840),
        Register('tmpz4', 32, 0x4860),
        Register('tmpq4', 16, 0x4860),
        Register('tmpd4', 8, 0x4860),
        Register('tmps4', 4, 0x4860),
        Register('tmpz5', 32, 0x4880),
        Register('tmpq5', 16, 0x4880),
        Register('tmpd5', 8, 0x4880),
        Register('tmps5', 4, 0x4880),
        Register('tmpz6', 32, 0x48a0),
        Register('tmpq6', 16, 0x48a0),
        Register('tmpd6', 8, 0x48a0),
        Register('tmps6', 4, 0x48a0),
        Register('z0', 32, 0x5000),
        Register('q0', 16, 0x5000),
        Register('d0', 8, 0x5000),
        Register('s0', 4, 0x5000),
        Register('h0', 2, 0x5000),
        Register('b0', 1, 0x5000),
        Register('z1', 32, 0x5020),
        Register('q1', 16, 0x5020),
        Register('d1', 8, 0x5020),
        Register('s1', 4, 0x5020),
        Register('h1', 2, 0x5020),
        Register('b1', 1, 0x5020),
        Register('z2', 32, 0x5040),
        Register('q2', 16, 0x5040),
        Register('d2', 8, 0x5040),
        Register('s2', 4, 0x5040),
        Register('h2', 2, 0x5040),
        Register('b2', 1, 0x5040),
        Register('z3', 32, 0x5060),
        Register('q3', 16, 0x5060),
        Register('d3', 8, 0x5060),
        Register('s3', 4, 0x5060),
        Register('h3', 2, 0x5060),
        Register('b3', 1, 0x5060),
        Register('z4', 32, 0x5080),
        Register('q4', 16, 0x5080),
        Register('d4', 8, 0x5080),
        Register('s4', 4, 0x5080),
        Register('h4', 2, 0x5080),
        Register('b4', 1, 0x5080),
        Register('z5', 32, 0x50a0),
        Register('q5', 16, 0x50a0),
        Register('d5', 8, 0x50a0),
        Register('s5', 4, 0x50a0),
        Register('h5', 2, 0x50a0),
        Register('b5', 1, 0x50a0),
        Register('z6', 32, 0x50c0),
        Register('q6', 16, 0x50c0),
        Register('d6', 8, 0x50c0),
        Register('s6', 4, 0x50c0),
        Register('h6', 2, 0x50c0),
        Register('b6', 1, 0x50c0),
        Register('z7', 32, 0x50e0),
        Register('q7', 16, 0x50e0),
        Register('d7', 8, 0x50e0),
        Register('s7', 4, 0x50e0),
        Register('h7', 2, 0x50e0),
        Register('b7', 1, 0x50e0),
        Register('z8', 32, 0x5100),
        Register('q8', 16, 0x5100),
        Register('d8', 8, 0x5100),
        Register('s8', 4, 0x5100),
        Register('h8', 2, 0x5100),
        Register('b8', 1, 0x5100),
        Register('z9', 32, 0x5120),
        Register('q9', 16, 0x5120),
        Register('d9', 8, 0x5120),
        Register('s9', 4, 0x5120),
        Register('h9', 2, 0x5120),
        Register('b9', 1, 0x5120),
        Register('z10', 32, 0x5140),
        Register('q10', 16, 0x5140),
        Register('d10', 8, 0x5140),
        Register('s10', 4, 0x5140),
        Register('h10', 2, 0x5140),
        Register('b10', 1, 0x5140),
        Register('z11', 32, 0x5160),
        Register('q11', 16, 0x5160),
        Register('d11', 8, 0x5160),
        Register('s11', 4, 0x5160),
        Register('h11', 2, 0x5160),
        Register('b11', 1, 0x5160),
        Register('z12', 32, 0x5180),
        Register('q12', 16, 0x5180),
        Register('d12', 8, 0x5180),
        Register('s12', 4, 0x5180),
        Register('h12', 2, 0x5180),
        Register('b12', 1, 0x5180),
        Register('z13', 32, 0x51a0),
        Register('q13', 16, 0x51a0),
        Register('d13', 8, 0x51a0),
        Register('s13', 4, 0x51a0),
        Register('h13', 2, 0x51a0),
        Register('b13', 1, 0x51a0),
        Register('z14', 32, 0x51c0),
        Register('q14', 16, 0x51c0),
        Register('d14', 8, 0x51c0),
        Register('s14', 4, 0x51c0),
        Register('h14', 2, 0x51c0),
        Register('b14', 1, 0x51c0),
        Register('z15', 32, 0x51e0),
        Register('q15', 16, 0x51e0),
        Register('d15', 8, 0x51e0),
        Register('s15', 4, 0x51e0),
        Register('h15', 2, 0x51e0),
        Register('b15', 1, 0x51e0),
        Register('z16', 32, 0x5200),
        Register('q16', 16, 0x5200),
        Register('d16', 8, 0x5200),
        Register('s16', 4, 0x5200),
        Register('h16', 2, 0x5200),
        Register('b16', 1, 0x5200),
        Register('z17', 32, 0x5220),
        Register('q17', 16, 0x5220),
        Register('d17', 8, 0x5220),
        Register('s17', 4, 0x5220),
        Register('h17', 2, 0x5220),
        Register('b17', 1, 0x5220),
        Register('z18', 32, 0x5240),
        Register('q18', 16, 0x5240),
        Register('d18', 8, 0x5240),
        Register('s18', 4, 0x5240),
        Register('h18', 2, 0x5240),
        Register('b18', 1, 0x5240),
        Register('z19', 32, 0x5260),
        Register('q19', 16, 0x5260),
        Register('d19', 8, 0x5260),
        Register('s19', 4, 0x5260),
        Register('h19', 2, 0x5260),
        Register('b19', 1, 0x5260),
        Register('z20', 32, 0x5280),
        Register('q20', 16, 0x5280),
        Register('d20', 8, 0x5280),
        Register('s20', 4, 0x5280),
        Register('h20', 2, 0x5280),
        Register('b20', 1, 0x5280),
        Register('z21', 32, 0x52a0),
        Register('q21', 16, 0x52a0),
        Register('d21', 8, 0x52a0),
        Register('s21', 4, 0x52a0),
        Register('h21', 2, 0x52a0),
        Register('b21', 1, 0x52a0),
        Register('z22', 32, 0x52c0),
        Register('q22', 16, 0x52c0),
        Register('d22', 8, 0x52c0),
        Register('s22', 4, 0x52c0),
        Register('h22', 2, 0x52c0),
        Register('b22', 1, 0x52c0),
        Register('z23', 32, 0x52e0),
        Register('q23', 16, 0x52e0),
        Register('d23', 8, 0x52e0),
        Register('s23', 4, 0x52e0),
        Register('h23', 2, 0x52e0),
        Register('b23', 1, 0x52e0),
        Register('z24', 32, 0x5300),
        Register('q24', 16, 0x5300),
        Register('d24', 8, 0x5300),
        Register('s24', 4, 0x5300),
        Register('h24', 2, 0x5300),
        Register('b24', 1, 0x5300),
        Register('z25', 32, 0x5320),
        Register('q25', 16, 0x5320),
        Register('d25', 8, 0x5320),
        Register('s25', 4, 0x5320),
        Register('h25', 2, 0x5320),
        Register('b25', 1, 0x5320),
        Register('z26', 32, 0x5340),
        Register('q26', 16, 0x5340),
        Register('d26', 8, 0x5340),
        Register('s26', 4, 0x5340),
        Register('h26', 2, 0x5340),
        Register('b26', 1, 0x5340),
        Register('z27', 32, 0x5360),
        Register('q27', 16, 0x5360),
        Register('d27', 8, 0x5360),
        Register('s27', 4, 0x5360),
        Register('h27', 2, 0x5360),
        Register('b27', 1, 0x5360),
        Register('z28', 32, 0x5380),
        Register('q28', 16, 0x5380),
        Register('d28', 8, 0x5380),
        Register('s28', 4, 0x5380),
        Register('h28', 2, 0x5380),
        Register('b28', 1, 0x5380),
        Register('z29', 32, 0x53a0),
        Register('q29', 16, 0x53a0),
        Register('d29', 8, 0x53a0),
        Register('s29', 4, 0x53a0),
        Register('h29', 2, 0x53a0),
        Register('b29', 1, 0x53a0),
        Register('z30', 32, 0x53c0),
        Register('q30', 16, 0x53c0),
        Register('d30', 8, 0x53c0),
        Register('s30', 4, 0x53c0),
        Register('h30', 2, 0x53c0),
        Register('b30', 1, 0x53c0),
        Register('z31', 32, 0x53e0),
        Register('q31', 16, 0x53e0),
        Register('d31', 8, 0x53e0),
        Register('s31', 4, 0x53e0),
        Register('h31', 2, 0x53e0),
        Register('b31', 1, 0x53e0),
        Register('p0', 4, 0x6000),
        Register('p1', 4, 0x6004),
        Register('p2', 4, 0x6008),
        Register('p3', 4, 0x600c),
        Register('p4', 4, 0x6010),
        Register('p5', 4, 0x6014),
        Register('p6', 4, 0x6018),
        Register('p7', 4, 0x601c),
        Register('p8', 4, 0x6020),
        Register('p9', 4, 0x6024),
        Register('p10', 4, 0x6028),
        Register('p11', 4, 0x602c),
        Register('p12', 4, 0x6030),
        Register('p13', 4, 0x6034),
        Register('p14', 4, 0x6038),
        Register('p15', 4, 0x603c)
    ]

register_arch(['aarch64:le:64:v8a'], 64, Endness.LE, ArchPcode_AARCH64_LE_64_v8A)
