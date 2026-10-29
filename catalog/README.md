# GO2ABROAD SOP Open Catalog

[![DOI](https://zenodo.org/badge/1438476437.svg)](https://doi.org/10.5281/zenodo.23767285)

This folder contains **143,726** SOPs. Every record includes:

1. **Introduction** (role / scenario / key controlled metric)
2. **Independent detail page URLs** in all **11 languages**
3. Compliance standard codes

Official portal: [https://sop.go2abroad.space](https://sop.go2abroad.space)

## Layout

| Path | Purpose |
| :--- | :--- |
| [`records/*.jsonl`](./records/) | Machine-readable shards (one country per file; one SOP per line) |
| [`industries/*.md`](./industries/) | Human-readable industry dossiers with deep links |
| [`countries/*.md`](./countries/) | Human-readable country dossiers with deep links |

## JSONL record schema

```json
{
  "sop_id": "AFG-0119-ENG-R3-ENG-SC-01",
  "country": "AFG",
  "industry_isic": "0119",
  "track": "ENG",
  "role": "Nutritional Analyst",
  "scenario": "...",
  "intro": "Nutritional Analyst — ... — Temperature: 23±2°C...",
  "tolerance": "Temperature: 23±2°C; Relative Humidity: 45±5% RH.",
  "standards": ["ISO 6496:1999", "ISO 13906:2008"],
  "urls": {
    "en": "https://sop.go2abroad.space/en/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "zh": "https://sop.go2abroad.space/zh/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "de": "https://sop.go2abroad.space/de/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "ja": "https://sop.go2abroad.space/ja/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "fr": "https://sop.go2abroad.space/fr/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "es": "https://sop.go2abroad.space/es/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "pt": "https://sop.go2abroad.space/pt/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "it": "https://sop.go2abroad.space/it/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "ko": "https://sop.go2abroad.space/ko/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "ar": "https://sop.go2abroad.space/ar/sop/AFG-0119-ENG-R3-ENG-SC-01.html",
    "hi": "https://sop.go2abroad.space/hi/sop/AFG-0119-ENG-R3-ENG-SC-01.html"
  }
}
```

## Countries (73)

[`AFG`](./countries/AFG.md) · [`AGO`](./countries/AGO.md) · [`ALB`](./countries/ALB.md) · [`AND`](./countries/AND.md) · [`ARE`](./countries/ARE.md) · [`ARG`](./countries/ARG.md) · [`ARM`](./countries/ARM.md) · [`ATG`](./countries/ATG.md) · [`AUS`](./countries/AUS.md) · [`AUT`](./countries/AUT.md) · [`AZE`](./countries/AZE.md) · [`BEL`](./countries/BEL.md) · [`BEN`](./countries/BEN.md) · [`BGD`](./countries/BGD.md) · [`BGR`](./countries/BGR.md) · [`BHR`](./countries/BHR.md) · [`BHS`](./countries/BHS.md) · [`BIH`](./countries/BIH.md) · [`BLR`](./countries/BLR.md) · [`BLZ`](./countries/BLZ.md) · [`BOL`](./countries/BOL.md) · [`BRA`](./countries/BRA.md) · [`BRB`](./countries/BRB.md) · [`BRN`](./countries/BRN.md) · [`BTN`](./countries/BTN.md) · [`BWA`](./countries/BWA.md) · [`CAN`](./countries/CAN.md) · [`CHE`](./countries/CHE.md) · [`CHL`](./countries/CHL.md) · [`CHN`](./countries/CHN.md) · [`CZE`](./countries/CZE.md) · [`DEU`](./countries/DEU.md) · [`DNK`](./countries/DNK.md) · [`DZA`](./countries/DZA.md) · [`EGY`](./countries/EGY.md) · [`ESP`](./countries/ESP.md) · [`FIN`](./countries/FIN.md) · [`FRA`](./countries/FRA.md) · [`GBR`](./countries/GBR.md) · [`GRC`](./countries/GRC.md) · [`HUN`](./countries/HUN.md) · [`IDN`](./countries/IDN.md) · [`IND`](./countries/IND.md) · [`IRL`](./countries/IRL.md) · [`ISR`](./countries/ISR.md) · [`ITA`](./countries/ITA.md) · [`JPN`](./countries/JPN.md) · [`KOR`](./countries/KOR.md) · [`KWT`](./countries/KWT.md) · [`LUX`](./countries/LUX.md) · [`MEX`](./countries/MEX.md) · [`MYS`](./countries/MYS.md) · [`NGA`](./countries/NGA.md) · [`NLD`](./countries/NLD.md) · [`NOR`](./countries/NOR.md) · [`NZL`](./countries/NZL.md) · [`OMN`](./countries/OMN.md) · [`PH`](./countries/PH.md) · [`PHL`](./countries/PHL.md) · [`POL`](./countries/POL.md) · [`PRT`](./countries/PRT.md) · [`QAT`](./countries/QAT.md) · [`ROU`](./countries/ROU.md) · [`SAU`](./countries/SAU.md) · [`SGP`](./countries/SGP.md) · [`SVK`](./countries/SVK.md) · [`SVN`](./countries/SVN.md) · [`SWE`](./countries/SWE.md) · [`THA`](./countries/THA.md) · [`TUR`](./countries/TUR.md) · [`USA`](./countries/USA.md) · [`VNM`](./countries/VNM.md) · [`ZAF`](./countries/ZAF.md)

## Industries (417)

[`0111`](./industries/0111.md) · [`0112`](./industries/0112.md) · [`0113`](./industries/0113.md) · [`0114`](./industries/0114.md) · [`0115`](./industries/0115.md) · [`0116`](./industries/0116.md) · [`0119`](./industries/0119.md) · [`0121`](./industries/0121.md) · [`0122`](./industries/0122.md) · [`0123`](./industries/0123.md) · [`0124`](./industries/0124.md) · [`0125`](./industries/0125.md) · [`0126`](./industries/0126.md) · [`0127`](./industries/0127.md) · [`0128`](./industries/0128.md) · [`0129`](./industries/0129.md) · [`0130`](./industries/0130.md) · [`0141`](./industries/0141.md) · [`0142`](./industries/0142.md) · [`0143`](./industries/0143.md) · [`0144`](./industries/0144.md) · [`0145`](./industries/0145.md) · [`0146`](./industries/0146.md) · [`0149`](./industries/0149.md) · [`0150`](./industries/0150.md) · [`0161`](./industries/0161.md) · [`0162`](./industries/0162.md) · [`0163`](./industries/0163.md) · [`0164`](./industries/0164.md) · [`0170`](./industries/0170.md) · [`0210`](./industries/0210.md) · [`0220`](./industries/0220.md) · [`0230`](./industries/0230.md) · [`0240`](./industries/0240.md) · [`0311`](./industries/0311.md) · [`0312`](./industries/0312.md) · [`0321`](./industries/0321.md) · [`0322`](./industries/0322.md) · [`0510`](./industries/0510.md) · [`0520`](./industries/0520.md) · [`0610`](./industries/0610.md) · [`0620`](./industries/0620.md) · [`0710`](./industries/0710.md) · [`0721`](./industries/0721.md) · [`0729`](./industries/0729.md) · [`0810`](./industries/0810.md) · [`0891`](./industries/0891.md) · [`0892`](./industries/0892.md) · [`0893`](./industries/0893.md) · [`0899`](./industries/0899.md) · [`0910`](./industries/0910.md) · [`0990`](./industries/0990.md) · [`1010`](./industries/1010.md) · [`1020`](./industries/1020.md) · [`1030`](./industries/1030.md) · [`1040`](./industries/1040.md) · [`1050`](./industries/1050.md) · [`1061`](./industries/1061.md) · [`1062`](./industries/1062.md) · [`1071`](./industries/1071.md) · [`1072`](./industries/1072.md) · [`1073`](./industries/1073.md) · [`1074`](./industries/1074.md) · [`1075`](./industries/1075.md) · [`1079`](./industries/1079.md) · [`1080`](./industries/1080.md) · [`1101`](./industries/1101.md) · [`1102`](./industries/1102.md) · [`1103`](./industries/1103.md) · [`1104`](./industries/1104.md) · [`1200`](./industries/1200.md) · [`1311`](./industries/1311.md) · [`1312`](./industries/1312.md) · [`1313`](./industries/1313.md) · [`1391`](./industries/1391.md) · [`1392`](./industries/1392.md) · [`1393`](./industries/1393.md) · [`1394`](./industries/1394.md) · [`1399`](./industries/1399.md) · [`1410`](./industries/1410.md) · [`1420`](./industries/1420.md) · [`1430`](./industries/1430.md) · [`1511`](./industries/1511.md) · [`1512`](./industries/1512.md) · [`1520`](./industries/1520.md) · [`1610`](./industries/1610.md) · [`1621`](./industries/1621.md) · [`1622`](./industries/1622.md) · [`1623`](./industries/1623.md) · [`1629`](./industries/1629.md) · [`1701`](./industries/1701.md) · [`1702`](./industries/1702.md) · [`1709`](./industries/1709.md) · [`1811`](./industries/1811.md) · [`1812`](./industries/1812.md) · [`1820`](./industries/1820.md) · [`1910`](./industries/1910.md) · [`1920`](./industries/1920.md) · [`2011`](./industries/2011.md) · [`2012`](./industries/2012.md) · [`2013`](./industries/2013.md) · [`2021`](./industries/2021.md) · [`2022`](./industries/2022.md) · [`2023`](./industries/2023.md) · [`2029`](./industries/2029.md) · [`2030`](./industries/2030.md) · [`2100`](./industries/2100.md) · [`2211`](./industries/2211.md) · [`2219`](./industries/2219.md) · [`2220`](./industries/2220.md) · [`2310`](./industries/2310.md) · [`2391`](./industries/2391.md) · [`2392`](./industries/2392.md) · [`2393`](./industries/2393.md) · [`2394`](./industries/2394.md) · [`2395`](./industries/2395.md) · [`2396`](./industries/2396.md) · [`2399`](./industries/2399.md) · [`2410`](./industries/2410.md) · [`2420`](./industries/2420.md) · [`2431`](./industries/2431.md) · [`2432`](./industries/2432.md) · [`2511`](./industries/2511.md) · [`2512`](./industries/2512.md) · [`2513`](./industries/2513.md) · [`2520`](./industries/2520.md) · [`2591`](./industries/2591.md) · [`2592`](./industries/2592.md) · [`2593`](./industries/2593.md) · [`2599`](./industries/2599.md) · [`2610`](./industries/2610.md) · [`2620`](./industries/2620.md) · [`2630`](./industries/2630.md) · [`2640`](./industries/2640.md) · [`2651`](./industries/2651.md) · [`2652`](./industries/2652.md) · [`2660`](./industries/2660.md) · [`2670`](./industries/2670.md) · [`2680`](./industries/2680.md) · [`2710`](./industries/2710.md) · [`2720`](./industries/2720.md) · [`2731`](./industries/2731.md) · [`2732`](./industries/2732.md) · [`2733`](./industries/2733.md) · [`2740`](./industries/2740.md) · [`2750`](./industries/2750.md) · [`2790`](./industries/2790.md) · [`2811`](./industries/2811.md) · [`2812`](./industries/2812.md) · [`2813`](./industries/2813.md) · [`2814`](./industries/2814.md) · [`2815`](./industries/2815.md) · [`2816`](./industries/2816.md) · [`2817`](./industries/2817.md) · [`2818`](./industries/2818.md) · [`2819`](./industries/2819.md) · [`2821`](./industries/2821.md) · [`2822`](./industries/2822.md) · [`2823`](./industries/2823.md) · [`2824`](./industries/2824.md) · [`2825`](./industries/2825.md) · [`2826`](./industries/2826.md) · [`2829`](./industries/2829.md) · [`2910`](./industries/2910.md) · [`2920`](./industries/2920.md) · [`2930`](./industries/2930.md) · [`3011`](./industries/3011.md) · [`3012`](./industries/3012.md) · [`3020`](./industries/3020.md) · [`3030`](./industries/3030.md) · [`3040`](./industries/3040.md) · [`3091`](./industries/3091.md) · [`3092`](./industries/3092.md) · [`3099`](./industries/3099.md) · [`3100`](./industries/3100.md) · [`3211`](./industries/3211.md) · [`3212`](./industries/3212.md) · [`3220`](./industries/3220.md) · [`3230`](./industries/3230.md) · [`3240`](./industries/3240.md) · [`3250`](./industries/3250.md) · [`3290`](./industries/3290.md) · [`3311`](./industries/3311.md) · [`3312`](./industries/3312.md) · [`3313`](./industries/3313.md) · [`3314`](./industries/3314.md) · [`3315`](./industries/3315.md) · [`3319`](./industries/3319.md) · [`3320`](./industries/3320.md) · [`3510`](./industries/3510.md) · [`3520`](./industries/3520.md) · [`3530`](./industries/3530.md) · [`3600`](./industries/3600.md) · [`3700`](./industries/3700.md) · [`3811`](./industries/3811.md) · [`3812`](./industries/3812.md) · [`3821`](./industries/3821.md) · [`3822`](./industries/3822.md) · [`3830`](./industries/3830.md) · [`3900`](./industries/3900.md) · [`4100`](./industries/4100.md) · [`4210`](./industries/4210.md) · [`4220`](./industries/4220.md) · [`4290`](./industries/4290.md) · [`4311`](./industries/4311.md) · [`4312`](./industries/4312.md) · [`4321`](./industries/4321.md) · [`4322`](./industries/4322.md) · [`4329`](./industries/4329.md) · [`4330`](./industries/4330.md) · [`4390`](./industries/4390.md) · [`4510`](./industries/4510.md) · [`4520`](./industries/4520.md) · [`4530`](./industries/4530.md) · [`4540`](./industries/4540.md) · [`4610`](./industries/4610.md) · [`4620`](./industries/4620.md) · [`4630`](./industries/4630.md) · [`4641`](./industries/4641.md) · [`4649`](./industries/4649.md) · [`4651`](./industries/4651.md) · [`4652`](./industries/4652.md) · [`4653`](./industries/4653.md) · [`4659`](./industries/4659.md) · [`4661`](./industries/4661.md) · [`4662`](./industries/4662.md) · [`4663`](./industries/4663.md) · [`4669`](./industries/4669.md) · [`4690`](./industries/4690.md) · [`4711`](./industries/4711.md) · [`4719`](./industries/4719.md) · [`4721`](./industries/4721.md) · [`4722`](./industries/4722.md) · [`4730`](./industries/4730.md) · [`4741`](./industries/4741.md) · [`4742`](./industries/4742.md) · [`4751`](./industries/4751.md) · [`4752`](./industries/4752.md) · [`4753`](./industries/4753.md) · [`4759`](./industries/4759.md) · [`4761`](./industries/4761.md) · [`4762`](./industries/4762.md) · [`4763`](./industries/4763.md) · [`4764`](./industries/4764.md) · [`4771`](./industries/4771.md) · [`4772`](./industries/4772.md) · [`4773`](./industries/4773.md) · [`4774`](./industries/4774.md) · [`4781`](./industries/4781.md) · [`4782`](./industries/4782.md) · [`4789`](./industries/4789.md) · [`4791`](./industries/4791.md) · [`4799`](./industries/4799.md) · [`4911`](./industries/4911.md) · [`4912`](./industries/4912.md) · [`4921`](./industries/4921.md) · [`4922`](./industries/4922.md) · [`4923`](./industries/4923.md) · [`4930`](./industries/4930.md) · [`5011`](./industries/5011.md) · [`5012`](./industries/5012.md) · [`5021`](./industries/5021.md) · [`5022`](./industries/5022.md) · [`5110`](./industries/5110.md) · [`5120`](./industries/5120.md) · [`5210`](./industries/5210.md) · [`5221`](./industries/5221.md) · [`5222`](./industries/5222.md) · [`5223`](./industries/5223.md) · [`5224`](./industries/5224.md) · [`5229`](./industries/5229.md) · [`5310`](./industries/5310.md) · [`5320`](./industries/5320.md) · [`5510`](./industries/5510.md) · [`5520`](./industries/5520.md) · [`5590`](./industries/5590.md) · [`5610`](./industries/5610.md) · [`5621`](./industries/5621.md) · [`5629`](./industries/5629.md) · [`5630`](./industries/5630.md) · [`5811`](./industries/5811.md) · [`5812`](./industries/5812.md) · [`5813`](./industries/5813.md) · [`5819`](./industries/5819.md) · [`5820`](./industries/5820.md) · [`5911`](./industries/5911.md) · [`5912`](./industries/5912.md) · [`5913`](./industries/5913.md) · [`5914`](./industries/5914.md) · [`5920`](./industries/5920.md) · [`6010`](./industries/6010.md) · [`6020`](./industries/6020.md) · [`6110`](./industries/6110.md) · [`6120`](./industries/6120.md) · [`6130`](./industries/6130.md) · [`6190`](./industries/6190.md) · [`6201`](./industries/6201.md) · [`6202`](./industries/6202.md) · [`6209`](./industries/6209.md) · [`6311`](./industries/6311.md) · [`6312`](./industries/6312.md) · [`6391`](./industries/6391.md) · [`6399`](./industries/6399.md) · [`6411`](./industries/6411.md) · [`6419`](./industries/6419.md) · [`6420`](./industries/6420.md) · [`6430`](./industries/6430.md) · [`6491`](./industries/6491.md) · [`6492`](./industries/6492.md) · [`6499`](./industries/6499.md) · [`6511`](./industries/6511.md) · [`6512`](./industries/6512.md) · [`6520`](./industries/6520.md) · [`6530`](./industries/6530.md) · [`6611`](./industries/6611.md) · [`6612`](./industries/6612.md) · [`6619`](./industries/6619.md) · [`6621`](./industries/6621.md) · [`6622`](./industries/6622.md) · [`6629`](./industries/6629.md) · [`6630`](./industries/6630.md) · [`6810`](./industries/6810.md) · [`6820`](./industries/6820.md) · [`6910`](./industries/6910.md) · [`6920`](./industries/6920.md) · [`7010`](./industries/7010.md) · [`7020`](./industries/7020.md) · [`7110`](./industries/7110.md) · [`7120`](./industries/7120.md) · [`7210`](./industries/7210.md) · [`7220`](./industries/7220.md) · [`7310`](./industries/7310.md) · [`7320`](./industries/7320.md) · [`7410`](./industries/7410.md) · [`7420`](./industries/7420.md) · [`7490`](./industries/7490.md) · [`7500`](./industries/7500.md) · [`7710`](./industries/7710.md) · [`7721`](./industries/7721.md) · [`7722`](./industries/7722.md) · [`7729`](./industries/7729.md) · [`7730`](./industries/7730.md) · [`7740`](./industries/7740.md) · [`7810`](./industries/7810.md) · [`7820`](./industries/7820.md) · [`7830`](./industries/7830.md) · [`7911`](./industries/7911.md) · [`7912`](./industries/7912.md) · [`7990`](./industries/7990.md) · [`8010`](./industries/8010.md) · [`8020`](./industries/8020.md) · [`8030`](./industries/8030.md) · [`8110`](./industries/8110.md) · [`8121`](./industries/8121.md) · [`8129`](./industries/8129.md) · [`8130`](./industries/8130.md) · [`8211`](./industries/8211.md) · [`8219`](./industries/8219.md) · [`8220`](./industries/8220.md) · [`8230`](./industries/8230.md) · [`8291`](./industries/8291.md) · [`8292`](./industries/8292.md) · [`8299`](./industries/8299.md) · [`8411`](./industries/8411.md) · [`8412`](./industries/8412.md) · [`8413`](./industries/8413.md) · [`8421`](./industries/8421.md) · [`8422`](./industries/8422.md) · [`8423`](./industries/8423.md) · [`8430`](./industries/8430.md) · [`8510`](./industries/8510.md) · [`8521`](./industries/8521.md) · [`8522`](./industries/8522.md) · [`8530`](./industries/8530.md) · [`8541`](./industries/8541.md) · [`8542`](./industries/8542.md) · [`8549`](./industries/8549.md) · [`8550`](./industries/8550.md) · [`8610`](./industries/8610.md) · [`8690`](./industries/8690.md) · [`8710`](./industries/8710.md) · [`8720`](./industries/8720.md) · [`8730`](./industries/8730.md) · [`8790`](./industries/8790.md) · [`8810`](./industries/8810.md) · [`8890`](./industries/8890.md) · [`9000`](./industries/9000.md) · [`9101`](./industries/9101.md) · [`9102`](./industries/9102.md) · [`9103`](./industries/9103.md) · [`9200`](./industries/9200.md) · [`9311`](./industries/9311.md) · [`9312`](./industries/9312.md) · [`9319`](./industries/9319.md) · [`9321`](./industries/9321.md) · [`9329`](./industries/9329.md) · [`9411`](./industries/9411.md) · [`9412`](./industries/9412.md) · [`9420`](./industries/9420.md) · [`9491`](./industries/9491.md) · [`9492`](./industries/9492.md) · [`9499`](./industries/9499.md) · [`9511`](./industries/9511.md) · [`9512`](./industries/9512.md) · [`9521`](./industries/9521.md) · [`9522`](./industries/9522.md) · [`9523`](./industries/9523.md) · [`9524`](./industries/9524.md) · [`9529`](./industries/9529.md) · [`9601`](./industries/9601.md) · [`9602`](./industries/9602.md) · [`9603`](./industries/9603.md) · [`9609`](./industries/9609.md) · [`9700`](./industries/9700.md) · [`9810`](./industries/9810.md) · [`9820`](./industries/9820.md) · [`9900`](./industries/9900.md)

## JSONL shards

- [`AFG.jsonl`](./records/AFG.jsonl) — **1,345** SOPs
- [`AGO.jsonl`](./records/AGO.jsonl) — **1,967** SOPs
- [`ALB.jsonl`](./records/ALB.jsonl) — **1,847** SOPs
- [`AND.jsonl`](./records/AND.jsonl) — **1,021** SOPs
- [`ARE.jsonl`](./records/ARE.jsonl) — **2,046** SOPs
- [`ARG.jsonl`](./records/ARG.jsonl) — **2,153** SOPs
- [`ARM.jsonl`](./records/ARM.jsonl) — **2,025** SOPs
- [`ATG.jsonl`](./records/ATG.jsonl) — **1,445** SOPs
- [`AUS.jsonl`](./records/AUS.jsonl) — **2,262** SOPs
- [`AUT.jsonl`](./records/AUT.jsonl) — **2,148** SOPs
- [`AZE.jsonl`](./records/AZE.jsonl) — **2,080** SOPs
- [`BEL.jsonl`](./records/BEL.jsonl) — **2,100** SOPs
- [`BEN.jsonl`](./records/BEN.jsonl) — **820** SOPs
- [`BGD.jsonl`](./records/BGD.jsonl) — **1,794** SOPs
- [`BGR.jsonl`](./records/BGR.jsonl) — **280** SOPs
- [`BHR.jsonl`](./records/BHR.jsonl) — **1,717** SOPs
- [`BHS.jsonl`](./records/BHS.jsonl) — **1,290** SOPs
- [`BIH.jsonl`](./records/BIH.jsonl) — **2,145** SOPs
- [`BLR.jsonl`](./records/BLR.jsonl) — **2,125** SOPs
- [`BLZ.jsonl`](./records/BLZ.jsonl) — **1,746** SOPs
- [`BOL.jsonl`](./records/BOL.jsonl) — **1,789** SOPs
- [`BRA.jsonl`](./records/BRA.jsonl) — **2,351** SOPs
- [`BRB.jsonl`](./records/BRB.jsonl) — **1,669** SOPs
- [`BRN.jsonl`](./records/BRN.jsonl) — **1,384** SOPs
- [`BTN.jsonl`](./records/BTN.jsonl) — **1,177** SOPs
- [`BWA.jsonl`](./records/BWA.jsonl) — **1,766** SOPs
- [`CAN.jsonl`](./records/CAN.jsonl) — **2,310** SOPs
- [`CHE.jsonl`](./records/CHE.jsonl) — **2,058** SOPs
- [`CHL.jsonl`](./records/CHL.jsonl) — **2,214** SOPs
- [`CHN.jsonl`](./records/CHN.jsonl) — **2,418** SOPs
- [`CZE.jsonl`](./records/CZE.jsonl) — **2,202** SOPs
- [`DEU.jsonl`](./records/DEU.jsonl) — **2,190** SOPs
- [`DNK.jsonl`](./records/DNK.jsonl) — **2,112** SOPs
- [`DZA.jsonl`](./records/DZA.jsonl) — **2,174** SOPs
- [`EGY.jsonl`](./records/EGY.jsonl) — **2,208** SOPs
- [`ESP.jsonl`](./records/ESP.jsonl) — **2,316** SOPs
- [`FIN.jsonl`](./records/FIN.jsonl) — **2,088** SOPs
- [`FRA.jsonl`](./records/FRA.jsonl) — **2,327** SOPs
- [`GBR.jsonl`](./records/GBR.jsonl) — **2,202** SOPs
- [`GRC.jsonl`](./records/GRC.jsonl) — **2,148** SOPs
- [`HUN.jsonl`](./records/HUN.jsonl) — **2,148** SOPs
- [`IDN.jsonl`](./records/IDN.jsonl) — **2,304** SOPs
- [`IND.jsonl`](./records/IND.jsonl) — **2,315** SOPs
- [`IRL.jsonl`](./records/IRL.jsonl) — **2,064** SOPs
- [`ISR.jsonl`](./records/ISR.jsonl) — **2,190** SOPs
- [`ITA.jsonl`](./records/ITA.jsonl) — **2,226** SOPs
- [`JPN.jsonl`](./records/JPN.jsonl) — **2,214** SOPs
- [`KOR.jsonl`](./records/KOR.jsonl) — **2,124** SOPs
- [`KWT.jsonl`](./records/KWT.jsonl) — **1,836** SOPs
- [`LUX.jsonl`](./records/LUX.jsonl) — **1,644** SOPs
- [`MEX.jsonl`](./records/MEX.jsonl) — **2,346** SOPs
- [`MYS.jsonl`](./records/MYS.jsonl) — **2,256** SOPs
- [`NGA.jsonl`](./records/NGA.jsonl) — **2,244** SOPs
- [`NLD.jsonl`](./records/NLD.jsonl) — **2,034** SOPs
- [`NOR.jsonl`](./records/NOR.jsonl) — **2,070** SOPs
- [`NZL.jsonl`](./records/NZL.jsonl) — **1,992** SOPs
- [`OMN.jsonl`](./records/OMN.jsonl) — **2,016** SOPs
- [`PH.jsonl`](./records/PH.jsonl) — **1** SOPs
- [`PHL.jsonl`](./records/PHL.jsonl) — **2,159** SOPs
- [`POL.jsonl`](./records/POL.jsonl) — **2,244** SOPs
- [`PRT.jsonl`](./records/PRT.jsonl) — **2,124** SOPs
- [`QAT.jsonl`](./records/QAT.jsonl) — **1,686** SOPs
- [`ROU.jsonl`](./records/ROU.jsonl) — **2,262** SOPs
- [`SAU.jsonl`](./records/SAU.jsonl) — **1,980** SOPs
- [`SGP.jsonl`](./records/SGP.jsonl) — **1,758** SOPs
- [`SVK.jsonl`](./records/SVK.jsonl) — **2,178** SOPs
- [`SVN.jsonl`](./records/SVN.jsonl) — **2,166** SOPs
- [`SWE.jsonl`](./records/SWE.jsonl) — **2,088** SOPs
- [`THA.jsonl`](./records/THA.jsonl) — **2,238** SOPs
- [`TUR.jsonl`](./records/TUR.jsonl) — **2,322** SOPs
- [`USA.jsonl`](./records/USA.jsonl) — **2,370** SOPs
- [`VNM.jsonl`](./records/VNM.jsonl) — **2,304** SOPs
- [`ZAF.jsonl`](./records/ZAF.jsonl) — **2,364** SOPs
