###
### This file was automatically generated
###

from archinfo.arch import register_arch, Endness, Register

from .common import ArchPcode


class ArchPcode_MIPS_LE_32_default(ArchPcode):
    name = 'MIPS:LE:32:default'
    pcode_arch = 'MIPS:LE:32:default'
    description = 'MIPS32 32-bit addresses, little endian, with mips16e'
    bits = 32
    ip_offset = 0x80
    sp_offset = 0x74
    bp_offset = sp_offset
    instruction_endness = Endness.LE
    register_list = [
        Register('zero', 4, 0x0),
        Register('at', 4, 0x4),
        Register('v0', 4, 0x8),
        Register('v1', 4, 0xc),
        Register('a0', 4, 0x10),
        Register('a1', 4, 0x14),
        Register('a2', 4, 0x18),
        Register('a3', 4, 0x1c),
        Register('t0', 4, 0x20),
        Register('t1', 4, 0x24),
        Register('t2', 4, 0x28),
        Register('t3', 4, 0x2c),
        Register('t4', 4, 0x30),
        Register('t5', 4, 0x34),
        Register('t6', 4, 0x38),
        Register('t7', 4, 0x3c),
        Register('s0', 4, 0x40),
        Register('s1', 4, 0x44),
        Register('s2', 4, 0x48),
        Register('s3', 4, 0x4c),
        Register('s4', 4, 0x50),
        Register('s5', 4, 0x54),
        Register('s6', 4, 0x58),
        Register('s7', 4, 0x5c),
        Register('t8', 4, 0x60),
        Register('t9', 4, 0x64),
        Register('k0', 4, 0x68),
        Register('k1', 4, 0x6c),
        Register('gp', 4, 0x70),
        Register('sp', 4, 0x74),
        Register('s8', 4, 0x78),
        Register('ra', 4, 0x7c),
        Register('pc', 4, 0x80, alias_names=('ip',)),
        Register('f0_1', 8, 0x1000),
        Register('f1', 4, 0x1000),
        Register('f0', 4, 0x1004),
        Register('f2_3', 8, 0x1008),
        Register('f3', 4, 0x1008),
        Register('f2', 4, 0x100c),
        Register('f4_5', 8, 0x1010),
        Register('f5', 4, 0x1010),
        Register('f4', 4, 0x1014),
        Register('f6_7', 8, 0x1018),
        Register('f7', 4, 0x1018),
        Register('f6', 4, 0x101c),
        Register('f8_9', 8, 0x1020),
        Register('f9', 4, 0x1020),
        Register('f8', 4, 0x1024),
        Register('f10_11', 8, 0x1028),
        Register('f11', 4, 0x1028),
        Register('f10', 4, 0x102c),
        Register('f12_13', 8, 0x1030),
        Register('f13', 4, 0x1030),
        Register('f12', 4, 0x1034),
        Register('f14_15', 8, 0x1038),
        Register('f15', 4, 0x1038),
        Register('f14', 4, 0x103c),
        Register('f16_17', 8, 0x1040),
        Register('f17', 4, 0x1040),
        Register('f16', 4, 0x1044),
        Register('f18_19', 8, 0x1048),
        Register('f19', 4, 0x1048),
        Register('f18', 4, 0x104c),
        Register('f20_21', 8, 0x1050),
        Register('f21', 4, 0x1050),
        Register('f20', 4, 0x1054),
        Register('f22_23', 8, 0x1058),
        Register('f23', 4, 0x1058),
        Register('f22', 4, 0x105c),
        Register('f24_25', 8, 0x1060),
        Register('f25', 4, 0x1060),
        Register('f24', 4, 0x1064),
        Register('f26_27', 8, 0x1068),
        Register('f27', 4, 0x1068),
        Register('f26', 4, 0x106c),
        Register('f28_29', 8, 0x1070),
        Register('f29', 4, 0x1070),
        Register('f28', 4, 0x1074),
        Register('f30_31', 8, 0x1078),
        Register('f31', 4, 0x1078),
        Register('f30', 4, 0x107c),
        Register('fir', 4, 0x1200),
        Register('fccr', 4, 0x1204),
        Register('fexr', 4, 0x1208),
        Register('fenr', 4, 0x120c),
        Register('fcsr', 4, 0x1210),
        Register('index', 4, 0x2000),
        Register('random', 4, 0x2004),
        Register('entrylo0', 4, 0x2008),
        Register('entrylo1', 4, 0x200c),
        Register('context', 4, 0x2010),
        Register('pagemask', 4, 0x2014),
        Register('wired', 4, 0x2018),
        Register('hwrena', 4, 0x201c),
        Register('badvaddr', 4, 0x2020),
        Register('count', 4, 0x2024),
        Register('entryhi', 4, 0x2028),
        Register('compare', 4, 0x202c),
        Register('status', 4, 0x2030),
        Register('cause', 4, 0x2034),
        Register('epc', 4, 0x2038),
        Register('prid', 4, 0x203c),
        Register('config', 4, 0x2040),
        Register('lladdr', 4, 0x2044),
        Register('watchlo', 4, 0x2048),
        Register('watchhi', 4, 0x204c),
        Register('xcontext', 4, 0x2050),
        Register('cop0_reg21', 4, 0x2054),
        Register('cop0_reg22', 4, 0x2058),
        Register('debug', 4, 0x205c),
        Register('depc', 4, 0x2060),
        Register('perfcnt', 4, 0x2064),
        Register('errctl', 4, 0x2068),
        Register('cacheerr', 4, 0x206c),
        Register('taglo', 4, 0x2070),
        Register('taghi', 4, 0x2074),
        Register('errorepc', 4, 0x2078),
        Register('desave', 4, 0x207c),
        Register('mvpcontrol', 4, 0x2100),
        Register('vpecontrol', 4, 0x2104),
        Register('tcstatus', 4, 0x2108),
        Register('cop0_reg3.1', 4, 0x210c),
        Register('contextconfig', 4, 0x2110),
        Register('pagegrain', 4, 0x2114),
        Register('srsconf0', 4, 0x2118),
        Register('cop0_reg7.1', 4, 0x211c),
        Register('cop0_reg8.1', 4, 0x2120),
        Register('cop0_reg9.1', 4, 0x2124),
        Register('cop0_reg10.1', 4, 0x2128),
        Register('cop0_reg11.1', 4, 0x212c),
        Register('intctl', 4, 0x2130),
        Register('cop0_reg13.1', 4, 0x2134),
        Register('cop0_reg14.1', 4, 0x2138),
        Register('ebase', 4, 0x213c),
        Register('config1', 4, 0x2140),
        Register('cop0_reg17.1', 4, 0x2144),
        Register('watchlo.1', 4, 0x2148),
        Register('watchhi.1', 4, 0x214c),
        Register('cop0_reg20.1', 4, 0x2150),
        Register('cop0_reg21.1', 4, 0x2154),
        Register('cop0_reg22.1', 4, 0x2158),
        Register('tracecontrol', 4, 0x215c),
        Register('cop0_reg24.1', 4, 0x2160),
        Register('perfcnt.1', 4, 0x2164),
        Register('cop0_reg26.1', 4, 0x2168),
        Register('cacheerr.1', 4, 0x216c),
        Register('datalo.1', 4, 0x2170),
        Register('datahi.1', 4, 0x2174),
        Register('cop0_reg30.1', 4, 0x2178),
        Register('cop0_reg31.1', 4, 0x217c),
        Register('mvpconf0', 4, 0x2200),
        Register('vpeconf0', 4, 0x2204),
        Register('tcbind', 4, 0x2208),
        Register('cop0_reg3.2', 4, 0x220c),
        Register('cop0_reg4.2', 4, 0x2210),
        Register('cop0_reg5.2', 4, 0x2214),
        Register('srsconf1', 4, 0x2218),
        Register('cop0_reg7.2', 4, 0x221c),
        Register('cop0_reg8.2', 4, 0x2220),
        Register('cop0_reg9.2', 4, 0x2224),
        Register('cop0_reg10.2', 4, 0x2228),
        Register('cop0_reg11.2', 4, 0x222c),
        Register('srsctl', 4, 0x2230),
        Register('cop0_reg13.2', 4, 0x2234),
        Register('cop0_reg14.2', 4, 0x2238),
        Register('cop0_reg15.2', 4, 0x223c),
        Register('config2', 4, 0x2240),
        Register('cop0_reg17.2', 4, 0x2244),
        Register('watchlo.2', 4, 0x2248),
        Register('watchhi.2', 4, 0x224c),
        Register('cop0_reg20.2', 4, 0x2250),
        Register('cop0_reg21.2', 4, 0x2254),
        Register('cop0_reg22.2', 4, 0x2258),
        Register('tracecontrol2', 4, 0x225c),
        Register('cop0_reg24.2', 4, 0x2260),
        Register('perfcnt.2', 4, 0x2264),
        Register('cop0_reg26.2', 4, 0x2268),
        Register('cacheerr.2', 4, 0x226c),
        Register('taglo.2', 4, 0x2270),
        Register('taghi.2', 4, 0x2274),
        Register('cop0_reg30.2', 4, 0x2278),
        Register('cop0_reg31.2', 4, 0x227c),
        Register('mvpconf1', 4, 0x2300),
        Register('vpeconf1', 4, 0x2304),
        Register('tcrestart', 4, 0x2308),
        Register('cop0_reg3.3', 4, 0x230c),
        Register('cop0_reg4.3', 4, 0x2310),
        Register('cop0_reg5.3', 4, 0x2314),
        Register('srsconf2', 4, 0x2318),
        Register('cop0_reg7.3', 4, 0x231c),
        Register('cop0_reg8.3', 4, 0x2320),
        Register('cop0_reg9.3', 4, 0x2324),
        Register('cop0_reg10.3', 4, 0x2328),
        Register('cop0_reg11.3', 4, 0x232c),
        Register('srsmap', 4, 0x2330),
        Register('cop0_reg13.3', 4, 0x2334),
        Register('cop0_reg14.3', 4, 0x2338),
        Register('cop0_reg15.3', 4, 0x233c),
        Register('config3', 4, 0x2340),
        Register('cop0_reg17.3', 4, 0x2344),
        Register('watchlo.3', 4, 0x2348),
        Register('watchhi.3', 4, 0x234c),
        Register('cop0_reg20.3', 4, 0x2350),
        Register('cop0_reg21.3', 4, 0x2354),
        Register('cop0_reg22.3', 4, 0x2358),
        Register('usertracedata', 4, 0x235c),
        Register('cop0_reg24.3', 4, 0x2360),
        Register('perfcnt.3', 4, 0x2364),
        Register('cop0_reg26.3', 4, 0x2368),
        Register('cacheerr.3', 4, 0x236c),
        Register('datalo.3', 4, 0x2370),
        Register('datahi.3', 4, 0x2374),
        Register('cop0_reg30.3', 4, 0x2378),
        Register('cop0_reg31.3', 4, 0x237c),
        Register('cop0_reg0.4', 4, 0x2400),
        Register('yqmask', 4, 0x2404),
        Register('tchalt', 4, 0x2408),
        Register('cop0_reg3.4', 4, 0x240c),
        Register('cop0_reg4.4', 4, 0x2410),
        Register('cop0_reg5.4', 4, 0x2414),
        Register('srsconf3', 4, 0x2418),
        Register('cop0_reg7.4', 4, 0x241c),
        Register('cop0_reg8.4', 4, 0x2420),
        Register('cop0_reg9.4', 4, 0x2424),
        Register('cop0_reg10.4', 4, 0x2428),
        Register('cop0_reg11.4', 4, 0x242c),
        Register('cop0_reg12.4', 4, 0x2430),
        Register('cop0_reg13.4', 4, 0x2434),
        Register('cop0_reg14.4', 4, 0x2438),
        Register('cop0_reg15.4', 4, 0x243c),
        Register('cop0_reg16.4', 4, 0x2440),
        Register('cop0_reg17.4', 4, 0x2444),
        Register('watchlo.4', 4, 0x2448),
        Register('watchhi.4', 4, 0x244c),
        Register('cop0_reg20.4', 4, 0x2450),
        Register('cop0_reg21.4', 4, 0x2454),
        Register('cop0_reg22.4', 4, 0x2458),
        Register('tracebpc', 4, 0x245c),
        Register('cop0_reg24.4', 4, 0x2460),
        Register('perfcnt.4', 4, 0x2464),
        Register('cop0_reg26.4', 4, 0x2468),
        Register('cacheerr.4', 4, 0x246c),
        Register('taglo.4', 4, 0x2470),
        Register('taghi.4', 4, 0x2474),
        Register('cop0_reg30.4', 4, 0x2478),
        Register('cop0_reg31.4', 4, 0x247c),
        Register('cop0_reg0.5', 4, 0x2500),
        Register('vpeschedule', 4, 0x2504),
        Register('tccontext', 4, 0x2508),
        Register('cop0_reg3.5', 4, 0x250c),
        Register('cop0_reg4.5', 4, 0x2510),
        Register('cop0_reg5.5', 4, 0x2514),
        Register('srsconf4', 4, 0x2518),
        Register('cop0_reg7.5', 4, 0x251c),
        Register('cop0_reg8.5', 4, 0x2520),
        Register('cop0_reg9.5', 4, 0x2524),
        Register('cop0_reg10.5', 4, 0x2528),
        Register('cop0_reg11.5', 4, 0x252c),
        Register('cop0_reg12.5', 4, 0x2530),
        Register('cop0_reg13.5', 4, 0x2534),
        Register('cop0_reg14.5', 4, 0x2538),
        Register('cop0_reg15.5', 4, 0x253c),
        Register('cop0_reg16.5', 4, 0x2540),
        Register('cop0_reg17.5', 4, 0x2544),
        Register('watchlo.5', 4, 0x2548),
        Register('watchhi.5', 4, 0x254c),
        Register('cop0_reg20.5', 4, 0x2550),
        Register('cop0_reg21.5', 4, 0x2554),
        Register('cop0_reg22.5', 4, 0x2558),
        Register('cop0_reg23.5', 4, 0x255c),
        Register('cop0_reg24.5', 4, 0x2560),
        Register('perfcnt.5', 4, 0x2564),
        Register('cop0_reg26.5', 4, 0x2568),
        Register('cacheerr.5', 4, 0x256c),
        Register('datalo.5', 4, 0x2570),
        Register('datahi.5', 4, 0x2574),
        Register('cop0_reg30.5', 4, 0x2578),
        Register('cop0_reg31.5', 4, 0x257c),
        Register('cop0_reg0.6', 4, 0x2600),
        Register('vpeschefback', 4, 0x2604),
        Register('tcschedule', 4, 0x2608),
        Register('cop0_reg3.6', 4, 0x260c),
        Register('cop0_reg4.6', 4, 0x2610),
        Register('cop0_reg5.6', 4, 0x2614),
        Register('cop0_reg6.6', 4, 0x2618),
        Register('cop0_reg7.6', 4, 0x261c),
        Register('cop0_reg8.6', 4, 0x2620),
        Register('cop0_reg9.6', 4, 0x2624),
        Register('cop0_reg10.6', 4, 0x2628),
        Register('cop0_reg11.6', 4, 0x262c),
        Register('cop0_reg12.6', 4, 0x2630),
        Register('cop0_reg13.6', 4, 0x2634),
        Register('cop0_reg14.6', 4, 0x2638),
        Register('cop0_reg15.6', 4, 0x263c),
        Register('cop0_reg16.6', 4, 0x2640),
        Register('cop0_reg17.6', 4, 0x2644),
        Register('watchlo.6', 4, 0x2648),
        Register('watchhi.6', 4, 0x264c),
        Register('cop0_reg20.6', 4, 0x2650),
        Register('cop0_reg21.6', 4, 0x2654),
        Register('cop0_reg22.6', 4, 0x2658),
        Register('cop0_reg23.6', 4, 0x265c),
        Register('cop0_reg24.6', 4, 0x2660),
        Register('perfcnt.6', 4, 0x2664),
        Register('cop0_reg26.6', 4, 0x2668),
        Register('cacheerr.6', 4, 0x266c),
        Register('taglo.6', 4, 0x2670),
        Register('taghi.6', 4, 0x2674),
        Register('cop0_reg30.6', 4, 0x2678),
        Register('cop0_reg31.6', 4, 0x267c),
        Register('cop0_reg0.7', 4, 0x2700),
        Register('vpeopt', 4, 0x2704),
        Register('tcschefback', 4, 0x2708),
        Register('cop0_reg3.7', 4, 0x270c),
        Register('cop0_reg4.7', 4, 0x2710),
        Register('cop0_reg5.7', 4, 0x2714),
        Register('cop0_reg6.7', 4, 0x2718),
        Register('cop0_reg7.7', 4, 0x271c),
        Register('cop0_reg8.7', 4, 0x2720),
        Register('cop0_reg9.7', 4, 0x2724),
        Register('cop0_reg10.7', 4, 0x2728),
        Register('cop0_reg11.7', 4, 0x272c),
        Register('cop0_reg12.7', 4, 0x2730),
        Register('cop0_reg13.7', 4, 0x2734),
        Register('cop0_reg14.7', 4, 0x2738),
        Register('cop0_reg15.7', 4, 0x273c),
        Register('cop0_reg16.7', 4, 0x2740),
        Register('cop0_reg17.7', 4, 0x2744),
        Register('watchlo.7', 4, 0x2748),
        Register('watchhi.7', 4, 0x274c),
        Register('cop0_reg20.7', 4, 0x2750),
        Register('cop0_reg21.7', 4, 0x2754),
        Register('cop0_reg22.7', 4, 0x2758),
        Register('cop0_reg23.7', 4, 0x275c),
        Register('cop0_reg24.7', 4, 0x2760),
        Register('perfcnt.7', 4, 0x2764),
        Register('cop0_reg26.7', 4, 0x2768),
        Register('cacheerr.7', 4, 0x276c),
        Register('datalo.7', 4, 0x2770),
        Register('datahi.7', 4, 0x2774),
        Register('cop0_reg30.7', 4, 0x2778),
        Register('cop0_reg31.7', 4, 0x277c),
        Register('hi', 4, 0x3000),
        Register('lo', 4, 0x3004),
        Register('hi1', 4, 0x3008),
        Register('lo1', 4, 0x300c),
        Register('hi2', 4, 0x3010),
        Register('lo2', 4, 0x3014),
        Register('hi3', 4, 0x3018),
        Register('lo3', 4, 0x301c),
        Register('tsp', 4, 0x3020),
        Register('isamodeswitch', 1, 0x3f00),
        Register('contextreg', 4, 0x4000)
    ]

register_arch(['mips:le:32:default'], 32, Endness.LE, ArchPcode_MIPS_LE_32_default)
