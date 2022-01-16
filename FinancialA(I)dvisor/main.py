import numpy as np
import smtplib, ssl
import sys


data = [
	["Wayne Boyer",
	 "ut.tincidunt.vehicula@protonmail.ca",
	 "Northwest Territories",
	 "Canada",
	"$62,268.94",
	"$4,057.88",
	"$437.62",
	"$58.84",
	"$235.49",
	"$878.13",
	"$892.93"
	 ],
	[
	"Rahim Gentry",
	"scelerisque@outlook.com",
	"Northwest Territories",
	"Canada",
	"$41,602.54",
	"$614.50",
	"$337.48",
	"$20.49",
	"$793.29",
	"$524.77",
	"$211.22"
	],
	[
	"Melinda Brooks",
	"dui.semper@outlook.org",
	"Quebec",
	"Canada",
	"$44,193.41",
	"$2,276.71",
	"$288.53",
	"$128.52",
	"$779.66",
	"$917.00",
	"$805.82"
	],
	[
	"Ella Wilcox",
	"eu.ultrices@hotmail.org",
	"Newfoundland and Labrador",
	"Canada",
	"$134,653.39",
	"$1,283.95",
	"$331.27",
	"$167.27",
	"$480.13",
	"$472.64",
	"$71.67"
	],
	[
	"Nola Battle",
	"sagittis@hotmail.ca",
	"Saskatchewan",
	"Canada",
	"$32,678.57",
	"$3,269.71",
	"$459.18",
	"$140.28",
	"$114.46",
	"$716.96",
	"$752.58"
	],
	[
	"Yoshi Howard",
	"ornare.lectus.justo@aol.couk",
	"New Brunswick",
	"Canada",
	"$102,635.33",
	"$3,418.59",
	"$451.05",
	"$264.41",
	"$316.76",
	"$721.98",
	"$133.59"
	],
	[
	"Faith Gilmore",
	"in.lobortis@google.ca",
	"Saskatchewan",
	"Canada",
	"$106,601.39",
	"$2,697.31",
	"$465.91",
	"$256.22",
	"$41.71",
	"$610.00",
	"$396.84"
	],
	[
	"Shafira Simmons",
	"integer.sem.elit@outlook.net",
	"Nunavut",
	"Canada",
	"$107,961.85",
	"$1,608.47",
	"$344.01",
	"$239.66",
	"$201.72",
	"$376.11",
	"$818.84"
	],
	[
	"Quin Morgan",
	"sit@yahoo.net",
	"Prince Edward Island",
	"Canada",
	"$148,351.58",
	"$2,418.49",
	"$459.96",
	"$297.19",
	"$155.27",
	"$516.43",
	"$693.81"
	],
	[
	"Howard Mccoy",
	"pharetra.nam@icloud.com",
	"New Brunswick",
	"Canada",
	"$22,570.78",
	"$4,198.51",
	"$172.29",
	"$125.03",
	"$31.32",
	"$982.60",
	"$564.11"
	],
	[
	"Keegan Rios",
	"tellus.nunc@google.edu",
	"Saskatchewan",
	"Canada",
	"$114,142.21",
	"$1,774.56",
	"$491.24",
	"$41.47",
	"$105.69",
	"$255.32",
	"$897.01"
	],
	[
	"Riley Hendrix",
	"mauris.nulla.integer@outlook.net",
	"Yukon",
	"Canada",
	"$42,991.14",
	"$4,466.70",
	"$302.93",
	"$182.67",
	"$465.30",
	"$879.10",
	"$826.77"
	],
	[
	"Carol Wise",
	"aliquam@icloud.net",
	"Newfoundland and Labrador",
	"Canada",
	"$86,021.28",
	"$3,762.53",
	"$109.57",
	"$129.64",
	"$464.88",
	"$271.31",
	"$778.15"
	],
	[
	"Veronica Witt",
	"morbi@google.net",
	"Nunavut",
	"Canada",
	"$46,879.90",
	"$2,118.16",
	"$313.94",
	"$151.76",
	"$253.43",
	"$792.88",
	"$774.91"
	],
	[
	"Kirestin Lopez",
	"aliquam@aol.ca",
	"Saskatchewan",
	"Canada",
	"$100,421.34",
	"$1,425.61",
	"$303.66",
	"$259.09",
	"$946.45",
	"$482.37",
	"$702.01"
	],
	[
	"Winter Mccullough",
	"nisl@outlook.couk",
	"Nunavut",
	"Canada",
	"$141,215.97",
	"$3,372.71",
	"$121.37",
	"$174.70",
	"$210.55",
	"$220.10",
	"$904.70"
	],
	[
	"Chanda Erickson",
	"at@aol.edu",
	"Yukon",
	"Canada",
	"$159,406.99",
	"$2,384.79",
	"$316.04",
	"$74.60",
	"$689.37",
	"$665.00",
	"$362.31"
	],
	[
	"John Fuentes",
	"ultrices.posuere@hotmail.ca",
	"Nova Scotia",
	"Canada",
	"$90,180.53",
	"$1,711.40",
	"$157.72",
	"$296.70",
	"$832.86",
	"$444.37",
	"$921.68"
	],
	[
	"Kiayada Tillman",
	"quis@protonmail.couk",
	"Yukon",
	"Canada",
	"$53,134.89",
	"$3,696.60",
	"$240.27",
	"$195.55",
	"$228.38",
	"$171.95",
	"$49.76"
	],
# 	[
# 		 "Odysseus Dillard",
# 		 "parturient.montes.nascetur@protonmail.net",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$122,723.86",
# 		 "$805.17",
# 		 "$386.77",
# 		 "$256.84",
# 		 "$891.05",
# 		 "$396.00",
# 		 "$126.29"
# 	],
# [
# 		 "Alisa Andrews",
# 		 "consectetuer.ipsum@outlook.org",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$101,405.62",
# 		 "$3,907.89",
# 		 "$391.06",
# 		 "$174.95",
# 		 "$945.28",
# 		 "$981.20",
# 		 "$822.73"
# 	],
# [
# 		 "Karen Pittman",
# 		 "mauris.blandit.enim@yahoo.com",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$28,450.30",
# 		 "$4,776.64",
# 		 "$404.99",
# 		 "$159.94",
# 		 "$628.32",
# 		 "$606.82",
# 		 "$395.04"
# 	],
# [
# 		 "Charlotte Britt",
# 		 "elementum.dui.quis@outlook.net",
# 		 "Prince Edward Island",
# 		 "Canada",
# 		 "$55,443.65",
# 		 "$4,639.30",
# 		 "$387.57",
# 		 "$24.77",
# 		 "$590.47",
# 		 "$314.18",
# 		 "$885.80"
# 	],
# [
# 		 "Edan Dunlap",
# 		 "vitae.erat@outlook.couk",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$110,474.73",
# 		 "$4,412.11",
# 		 "$340.68",
# 		 "$249.92",
# 		 "$864.78",
# 		 "$837.72",
# 		 "$126.97"
# 	],
# [
# 		 "Shannon Blevins",
# 		 "bibendum@yahoo.edu",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$27,854.40",
# 		 "$2,334.33",
# 		 "$128.52",
# 		 "$215.16",
# 		 "$302.35",
# 		 "$641.01",
# 		 "$176.58"
# 	],
# [
# 		 "Meghan Short",
# 		 "nisi.mauris@aol.org",
# 		 "Ontario",
# 		 "Canada",
# 		 "$85,527.44",
# 		 "$2,103.30",
# 		 "$270.74",
# 		 "$171.45",
# 		 "$820.25",
# 		 "$366.76",
# 		 "$168.00"
# 	],
# [
# 		 "Xander Simmons",
# 		 "iaculis.aliquet.diam@hotmail.org",
# 		 "Quebec",
# 		 "Canada",
# 		 "$90,899.79",
# 		 "$3,117.02",
# 		 "$297.75",
# 		 "$129.06",
# 		 "$432.80",
# 		 "$940.72",
# 		 "$436.23"
# 	],
# [
# 		 "Nigel Lawson",
# 		 "eget.laoreet@outlook.net",
# 		 "Yukon",
# 		 "Canada",
# 		 "$146,464.62",
# 		 "$2,110.16",
# 		 "$209.04",
# 		 "$197.57",
# 		 "$806.37",
# 		 "$428.28",
# 		 "$706.72"
# 	],
# [
# 		 "Slade Ellison",
# 		 "et.eros@icloud.org",
# 		 "Yukon",
# 		 "Canada",
# 		 "$83,832.58",
# 		 "$4,508.32",
# 		 "$126.11",
# 		 "$268.19",
# 		 "$880.35",
# 		 "$472.65",
# 		 "$899.82"
# 	],
# [
# 		 "Elvis Robertson",
# 		 "purus.maecenas.libero@icloud.ca",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$20,104.53",
# 		 "$3,059.59",
# 		 "$293.68",
# 		 "$241.83",
# 		 "$327.42",
# 		 "$430.88",
# 		 "$940.49"
# 	],
# [
# 		 "Xander Pruitt",
# 		 "egestas@yahoo.com",
# 		 "Ontario",
# 		 "Canada",
# 		 "$72,942.56",
# 		 "$1,624.21",
# 		 "$389.93",
# 		 "$107.43",
# 		 "$603.30",
# 		 "$319.44",
# 		 "$798.77"
# 	],
# [
# 		 "Velma Langley",
# 		 "feugiat.metus@protonmail.ca",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$110,997.76",
# 		 "$761.24",
# 		 "$210.47",
# 		 "$263.46",
# 		 "$646.52",
# 		 "$738.54",
# 		 "$941.47"
# 	],
# [
# 		 "Samuel Ford",
# 		 "et.euismod.et@outlook.edu",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$104,682.14",
# 		 "$3,675.31",
# 		 "$193.35",
# 		 "$137.04",
# 		 "$512.24",
# 		 "$837.60",
# 		 "$331.73"
# 	],
# [
# 		 "Lawrence Holloway",
# 		 "augue.eu@yahoo.couk",
# 		 "Ontario",
# 		 "Canada",
# 		 "$178,190.58",
# 		 "$1,120.78",
# 		 "$104.77",
# 		 "$144.04",
# 		 "$159.17",
# 		 "$940.58",
# 		 "$643.42"
# 	],
# [
# 		 "Maggie Flores",
# 		 "metus@hotmail.com",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$119,160.71",
# 		 "$2,857.28",
# 		 "$422.36",
# 		 "$248.32",
# 		 "$571.96",
# 		 "$209.29",
# 		 "$490.62"
# 	],
# [
# 		 "Martin Blackburn",
# 		 "pellentesque@yahoo.net",
# 		 "Alberta",
# 		 "Canada",
# 		 "$129,976.55",
# 		 "$2,387.65",
# 		 "$303.98",
# 		 "$205.52",
# 		 "$859.16",
# 		 "$824.28",
# 		 "$845.40"
# 	],
# [
# 		 "Ivan Mclaughlin",
# 		 "sem@hotmail.ca",
# 		 "Quebec",
# 		 "Canada",
# 		 "$47,638.48",
# 		 "$1,051.06",
# 		 "$230.58",
# 		 "$294.78",
# 		 "$548.28",
# 		 "$981.38",
# 		 "$326.85"
# 	],
# [
# 		 "Jorden Black",
# 		 "cubilia.curae.phasellus@icloud.org",
# 		 "Yukon",
# 		 "Canada",
# 		 "$175,331.16",
# 		 "$3,215.41",
# 		 "$302.26",
# 		 "$299.59",
# 		 "$762.91",
# 		 "$167.66",
# 		 "$486.79"
# 	],
# [
# 		 "Justin Delgado",
# 		 "ad@google.couk",
# 		 "Quebec",
# 		 "Canada",
# 		 "$99,522.25",
# 		 "$4,166.55",
# 		 "$467.73",
# 		 "$229.41",
# 		 "$795.80",
# 		 "$594.52",
# 		 "$359.38"
# 	],
# [
# 		 "Mufutau Guzman",
# 		 "facilisis.magna.tellus@icloud.couk",
# 		 "Yukon",
# 		 "Canada",
# 		 "$38,511.33",
# 		 "$627.22",
# 		 "$139.36",
# 		 "$83.20",
# 		 "$917.59",
# 		 "$168.84",
# 		 "$852.78"
# 	],
# [
# 		 "Lacey Salinas",
# 		 "quam.curabitur.vel@protonmail.edu",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$62,977.38",
# 		 "$525.74",
# 		 "$286.20",
# 		 "$284.92",
# 		 "$251.46",
# 		 "$421.57",
# 		 "$199.00"
# 	],
# [
# 		 "Sonya Hopper",
# 		 "sed.nulla@outlook.org",
# 		 "Prince Edward Island",
# 		 "Canada",
# 		 "$122,470.98",
# 		 "$4,864.32",
# 		 "$460.16",
# 		 "$217.73",
# 		 "$899.17",
# 		 "$449.35",
# 		 "$484.67"
# 	],
# [
# 		 "Henry Wilkins",
# 		 "vulputate@icloud.com",
# 		 "Quebec",
# 		 "Canada",
# 		 "$154,489.71",
# 		 "$1,024.05",
# 		 "$482.05",
# 		 "$78.08",
# 		 "$545.53",
# 		 "$521.12",
# 		 "$622.18"
# 	],
# [
# 		 "Lael Blair",
# 		 "proin@google.edu",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$103,148.62",
# 		 "$1,267.65",
# 		 "$232.08",
# 		 "$65.81",
# 		 "$272.82",
# 		 "$477.23",
# 		 "$202.55"
# 	],
# [
# 		 "Malik Foley",
# 		 "vel.pede.blandit@icloud.couk",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$162,559.94",
# 		 "$1,612.62",
# 		 "$463.60",
# 		 "$101.16",
# 		 "$939.53",
# 		 "$881.87",
# 		 "$613.57"
# 	],
# [
# 		 "Russell Stanton",
# 		 "molestie.sed@outlook.edu",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$79,171.77",
# 		 "$773.57",
# 		 "$238.75",
# 		 "$269.66",
# 		 "$797.76",
# 		 "$168.68",
# 		 "$340.29"
# 	],
# [
# 		 "Karyn Bernard",
# 		 "eros.nam@outlook.ca",
# 		 "Alberta",
# 		 "Canada",
# 		 "$152,529.02",
# 		 "$1,287.60",
# 		 "$405.90",
# 		 "$261.02",
# 		 "$160.29",
# 		 "$314.93",
# 		 "$168.24"
# 	],
# [
# 		 "Daryl Strickland",
# 		 "volutpat.nulla@yahoo.couk",
# 		 "Ontario",
# 		 "Canada",
# 		 "$27,448.94",
# 		 "$2,939.20",
# 		 "$201.89",
# 		 "$261.43",
# 		 "$615.29",
# 		 "$363.60",
# 		 "$254.18"
# 	],
# [
# 		 "Isaac Moody",
# 		 "purus.ac@hotmail.edu",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$91,756.64",
# 		 "$3,324.23",
# 		 "$335.00",
# 		 "$276.08",
# 		 "$595.57",
# 		 "$698.46",
# 		 "$198.64"
# 	],
# [
# 		 "Tarik Hogan",
# 		 "non@protonmail.couk",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$116,106.03",
# 		 "$4,974.44",
# 		 "$458.83",
# 		 "$256.16",
# 		 "$113.13",
# 		 "$709.92",
# 		 "$710.18"
# 	],
# [
# 		 "Frances Copeland",
# 		 "eget.volutpat@yahoo.com",
# 		 "Ontario",
# 		 "Canada",
# 		 "$151,959.28",
# 		 "$2,077.15",
# 		 "$313.23",
# 		 "$30.56",
# 		 "$466.45",
# 		 "$728.65",
# 		 "$795.39"
# 	],
# [
# 		 "Angela Lyons",
# 		 "est.mollis@aol.edu",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$34,500.53",
# 		 "$4,855.93",
# 		 "$226.56",
# 		 "$174.41",
# 		 "$877.85",
# 		 "$427.69",
# 		 "$531.45"
# 	],
# [
# 		 "Joel Fitzgerald",
# 		 "proin.non@icloud.com",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$122,324.97",
# 		 "$3,216.33",
# 		 "$338.79",
# 		 "$143.95",
# 		 "$820.15",
# 		 "$758.94",
# 		 "$251.45"
# 	],
# [
# 		 "Caleb Moore",
# 		 "tristique.senectus@outlook.net",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$56,659.56",
# 		 "$1,620.58",
# 		 "$361.74",
# 		 "$123.35",
# 		 "$713.58",
# 		 "$456.14",
# 		 "$886.64"
# 	],
# [
# 		 "Buffy Sosa",
# 		 "magna.tellus@google.ca",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$64,176.35",
# 		 "$3,158.20",
# 		 "$260.11",
# 		 "$154.16",
# 		 "$62.44",
# 		 "$731.45",
# 		 "$866.74"
# 	],
# [
# 		 "Lenore Armstrong",
# 		 "nec.quam@outlook.couk",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$25,664.42",
# 		 "$2,953.61",
# 		 "$200.29",
# 		 "$284.58",
# 		 "$641.68",
# 		 "$286.53",
# 		 "$865.61"
# 	],
# [
# 		 "Amos Ayala",
# 		 "sollicitudin.orci.sem@icloud.com",
# 		 "Alberta",
# 		 "Canada",
# 		 "$150,382.39",
# 		 "$2,946.35",
# 		 "$218.63",
# 		 "$191.18",
# 		 "$918.78",
# 		 "$472.62",
# 		 "$475.71"
# 	],
# [
# 		 "Lionel Herring",
# 		 "auctor.nunc.nulla@google.edu",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$55,007.56",
# 		 "$2,701.93",
# 		 "$283.42",
# 		 "$242.46",
# 		 "$706.16",
# 		 "$214.98",
# 		 "$310.11"
# 	],
# [
# 		 "Asher Bright",
# 		 "rutrum.magna@google.couk",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$159,458.38",
# 		 "$4,879.09",
# 		 "$475.46",
# 		 "$266.91",
# 		 "$91.95",
# 		 "$731.89",
# 		 "$464.74"
# 	],
# [
# 		 "Lysandra Rosario",
# 		 "gravida@yahoo.net",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$63,082.71",
# 		 "$2,441.53",
# 		 "$224.48",
# 		 "$89.68",
# 		 "$487.99",
# 		 "$615.33",
# 		 "$35.19"
# 	],
# [
# 		 "Igor Fields",
# 		 "a.purus@aol.couk",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$83,419.34",
# 		 "$4,877.58",
# 		 "$158.24",
# 		 "$179.31",
# 		 "$296.33",
# 		 "$733.12",
# 		 "$573.04"
# 	],
# [
# 		 "Griffith Jordan",
# 		 "turpis.in@outlook.com",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$30,296.84",
# 		 "$2,115.29",
# 		 "$380.50",
# 		 "$56.69",
# 		 "$108.65",
# 		 "$420.28",
# 		 "$295.07"
# 	],
# [
# 		 "Lisandra Morgan",
# 		 "venenatis.vel@protonmail.couk",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$147,459.62",
# 		 "$2,670.25",
# 		 "$268.60",
# 		 "$71.02",
# 		 "$872.70",
# 		 "$907.08",
# 		 "$373.77"
# 	],
# [
# 		 "Christopher Dejesus",
# 		 "scelerisque.scelerisque.dui@protonmail.net",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$84,089.54",
# 		 "$3,060.54",
# 		 "$322.21",
# 		 "$154.16",
# 		 "$458.33",
# 		 "$479.59",
# 		 "$905.68"
# 	],
# [
# 		 "Michael Finley",
# 		 "sagittis.nullam.vitae@icloud.org",
# 		 "Alberta",
# 		 "Canada",
# 		 "$134,407.47",
# 		 "$964.92",
# 		 "$367.58",
# 		 "$258.92",
# 		 "$993.67",
# 		 "$652.86",
# 		 "$843.84"
# 	],
# [
# 		 "Kiayada Jacobs",
# 		 "tincidunt@protonmail.couk",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$141,277.67",
# 		 "$3,334.17",
# 		 "$492.19",
# 		 "$81.67",
# 		 "$549.70",
# 		 "$732.41",
# 		 "$353.67"
# 	],
# [
# 		 "Jarrod David",
# 		 "sit.amet.risus@protonmail.com",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$37,049.73",
# 		 "$2,469.18",
# 		 "$451.24",
# 		 "$212.25",
# 		 "$476.73",
# 		 "$460.64",
# 		 "$322.53"
# 	],
# [
# 		 "Vladimir Vaughn",
# 		 "ante.bibendum@outlook.edu",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$173,731.48",
# 		 "$2,067.10",
# 		 "$346.67",
# 		 "$27.87",
# 		 "$665.62",
# 		 "$183.25",
# 		 "$685.40"
# 	],
# [
# 		 "Joel Townsend",
# 		 "amet.dapibus@aol.ca",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$103,789.89",
# 		 "$1,118.84",
# 		 "$276.43",
# 		 "$82.62",
# 		 "$217.58",
# 		 "$686.07",
# 		 "$91.09"
# 	],
# [
# 		 "Wayne Hill",
# 		 "cras@yahoo.net",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$48,095.89",
# 		 "$4,274.09",
# 		 "$397.80",
# 		 "$244.79",
# 		 "$745.27",
# 		 "$952.06",
# 		 "$253.59"
# 	],
# [
# 		 "Basia Rowland",
# 		 "facilisis.eget@google.net",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$113,103.55",
# 		 "$839.28",
# 		 "$249.33",
# 		 "$179.28",
# 		 "$445.48",
# 		 "$195.89",
# 		 "$260.75"
# 	],
# [
# 		 "Walter Bolton",
# 		 "sed.est@hotmail.ca",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$106,325.35",
# 		 "$1,419.02",
# 		 "$446.49",
# 		 "$293.89",
# 		 "$352.99",
# 		 "$355.26",
# 		 "$988.99"
# 	],
# [
# 		 "Ramona Medina",
# 		 "magna.malesuada@yahoo.couk",
# 		 "Ontario",
# 		 "Canada",
# 		 "$116,221.55",
# 		 "$2,440.02",
# 		 "$242.20",
# 		 "$222.68",
# 		 "$135.11",
# 		 "$615.61",
# 		 "$957.03"
# 	],
# [
# 		 "MacKensie Graham",
# 		 "et.rutrum@google.couk",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$27,215.83",
# 		 "$1,053.10",
# 		 "$177.41",
# 		 "$187.18",
# 		 "$241.83",
# 		 "$539.83",
# 		 "$402.49"
# 	],
# [
# 		 "Geraldine Farrell",
# 		 "donec@google.net",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$56,933.86",
# 		 "$4,589.85",
# 		 "$305.20",
# 		 "$298.20",
# 		 "$87.42",
# 		 "$755.68",
# 		 "$968.36"
# 	],
# [
# 		 "Amy Richmond",
# 		 "pede.ac@yahoo.org",
# 		 "Alberta",
# 		 "Canada",
# 		 "$70,343.61",
# 		 "$2,063.33",
# 		 "$378.04",
# 		 "$114.04",
# 		 "$749.17",
# 		 "$229.46",
# 		 "$931.24"
# 	],
# [
# 		 "Rajah Madden",
# 		 "mi.enim@icloud.org",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$105,561.28",
# 		 "$2,217.37",
# 		 "$402.38",
# 		 "$92.71",
# 		 "$924.69",
# 		 "$443.99",
# 		 "$287.00"
# 	],
# [
# 		 "Kelly Crosby",
# 		 "molestie@google.net",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$110,696.80",
# 		 "$1,030.96",
# 		 "$326.22",
# 		 "$84.65",
# 		 "$503.24",
# 		 "$157.91",
# 		 "$273.31"
# 	],
# [
# 		 "Adena Dalton",
# 		 "eu.lacus.quisque@outlook.couk",
# 		 "Quebec",
# 		 "Canada",
# 		 "$178,186.89",
# 		 "$4,261.67",
# 		 "$307.08",
# 		 "$249.07",
# 		 "$510.23",
# 		 "$735.60",
# 		 "$33.06"
# 	],
# [
# 		 "Thane Garrison",
# 		 "eu@protonmail.edu",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$177,373.01",
# 		 "$4,236.25",
# 		 "$408.32",
# 		 "$181.45",
# 		 "$216.83",
# 		 "$714.73",
# 		 "$204.91"
# 	],
# [
# 		 "Warren Santana",
# 		 "aliquet.vel.vulputate@yahoo.ca",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$92,315.44",
# 		 "$2,316.22",
# 		 "$350.69",
# 		 "$240.15",
# 		 "$100.35",
# 		 "$230.75",
# 		 "$469.79"
# 	],
# [
# 		 "Ursula Espinoza",
# 		 "molestie@icloud.edu",
# 		 "Prince Edward Island",
# 		 "Canada",
# 		 "$98,627.02",
# 		 "$2,638.39",
# 		 "$323.72",
# 		 "$278.13",
# 		 "$588.67",
# 		 "$866.93",
# 		 "$535.48"
# 	],
# [
# 		 "Robert Curtis",
# 		 "mollis@outlook.couk",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$63,710.94",
# 		 "$2,764.30",
# 		 "$256.75",
# 		 "$218.33",
# 		 "$221.45",
# 		 "$423.76",
# 		 "$805.05"
# 	],
# [
# 		 "Geoffrey Robles",
# 		 "egestas@icloud.net",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$109,186.92",
# 		 "$3,697.88",
# 		 "$149.13",
# 		 "$282.87",
# 		 "$999.33",
# 		 "$479.04",
# 		 "$682.69"
# 	],
# [
# 		 "Burton Porter",
# 		 "sodales.mauris@google.com",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$101,782.56",
# 		 "$4,081.44",
# 		 "$275.76",
# 		 "$258.79",
# 		 "$423.41",
# 		 "$820.52",
# 		 "$350.51"
# 	],
# [
# 		 "Donna Mitchell",
# 		 "volutpat@outlook.couk",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$70,556.65",
# 		 "$1,762.67",
# 		 "$110.71",
# 		 "$81.20",
# 		 "$794.78",
# 		 "$168.04",
# 		 "$785.91"
# 	],
# [
# 		 "Benjamin Park",
# 		 "lorem@aol.com",
# 		 "Quebec",
# 		 "Canada",
# 		 "$50,091.95",
# 		 "$1,867.18",
# 		 "$299.04",
# 		 "$153.18",
# 		 "$854.88",
# 		 "$162.38",
# 		 "$127.74"
# 	],
# [
# 		 "Blake Schroeder",
# 		 "ultrices@google.edu",
# 		 "Alberta",
# 		 "Canada",
# 		 "$53,208.03",
# 		 "$3,573.66",
# 		 "$314.18",
# 		 "$51.78",
# 		 "$255.45",
# 		 "$781.20",
# 		 "$223.60"
# 	],
# [
# 		 "Philip Acosta",
# 		 "massa.quisque.porttitor@outlook.net",
# 		 "Alberta",
# 		 "Canada",
# 		 "$45,983.44",
# 		 "$3,862.58",
# 		 "$237.50",
# 		 "$260.64",
# 		 "$149.00",
# 		 "$959.16",
# 		 "$520.40"
# 	],
# [
# 		 "Neve Franks",
# 		 "faucibus.leo@google.net",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$67,111.86",
# 		 "$3,777.79",
# 		 "$208.98",
# 		 "$25.51",
# 		 "$100.52",
# 		 "$605.10",
# 		 "$239.33"
# 	],
# [
# 		 "Solomon Rowland",
# 		 "cum.sociis@hotmail.ca",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$142,287.34",
# 		 "$3,195.61",
# 		 "$458.59",
# 		 "$51.82",
# 		 "$843.80",
# 		 "$826.35",
# 		 "$94.00"
# 	],
# [
# 		 "Joel Davidson",
# 		 "nulla@protonmail.org",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$101,997.71",
# 		 "$3,459.21",
# 		 "$338.93",
# 		 "$230.94",
# 		 "$679.97",
# 		 "$285.68",
# 		 "$125.11"
# 	],
# [
# 		 "Quamar Petty",
# 		 "accumsan.laoreet@google.com",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$103,813.72",
# 		 "$842.89",
# 		 "$347.82",
# 		 "$283.80",
# 		 "$791.76",
# 		 "$387.66",
# 		 "$807.73"
# 	],
# [
# 		 "Cooper Valdez",
# 		 "phasellus.at@hotmail.org",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$36,441.93",
# 		 "$3,695.36",
# 		 "$147.53",
# 		 "$218.45",
# 		 "$166.44",
# 		 "$963.81",
# 		 "$253.56"
# 	],
# [
# 		 "Amaya Mccall",
# 		 "magna.duis.dignissim@outlook.net",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$142,548.95",
# 		 "$3,422.41",
# 		 "$155.76",
# 		 "$95.32",
# 		 "$317.09",
# 		 "$348.93",
# 		 "$205.43"
# 	],
# [
# 		 "Danielle Mcpherson",
# 		 "nunc.ut@protonmail.couk",
# 		 "Alberta",
# 		 "Canada",
# 		 "$68,661.77",
# 		 "$2,547.38",
# 		 "$142.31",
# 		 "$118.98",
# 		 "$169.98",
# 		 "$232.77",
# 		 "$118.16"
# 	],
# [
# 		 "Chandler Dunlap",
# 		 "cubilia.curae@hotmail.ca",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$71,843.33",
# 		 "$4,135.34",
# 		 "$433.22",
# 		 "$186.81",
# 		 "$710.52",
# 		 "$761.60",
# 		 "$650.71"
# 	],
# [
# 		 "Paula Rollins",
# 		 "in.condimentum@icloud.net",
# 		 "Yukon",
# 		 "Canada",
# 		 "$38,921.87",
# 		 "$1,807.55",
# 		 "$397.17",
# 		 "$228.06",
# 		 "$216.69",
# 		 "$577.19",
# 		 "$796.33"
# 	],
# [
# 		 "Noah Bailey",
# 		 "elementum.at@aol.edu",
# 		 "Alberta",
# 		 "Canada",
# 		 "$31,829.23",
# 		 "$1,061.62",
# 		 "$308.29",
# 		 "$89.93",
# 		 "$880.22",
# 		 "$903.02",
# 		 "$92.56"
# 	],
# [
# 		 "Jerome Burt",
# 		 "convallis@yahoo.couk",
# 		 "Alberta",
# 		 "Canada",
# 		 "$115,327.04",
# 		 "$517.95",
# 		 "$471.13",
# 		 "$179.10",
# 		 "$506.51",
# 		 "$531.33",
# 		 "$926.71"
# 	],
# [
# 		 "Austin Meadows",
# 		 "sed@outlook.net",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$69,261.57",
# 		 "$2,258.23",
# 		 "$401.60",
# 		 "$26.52",
# 		 "$478.11",
# 		 "$960.71",
# 		 "$259.89"
# 	],
# [
# 		 "Tobias Arnold",
# 		 "elit.elit@google.edu",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$123,023.80",
# 		 "$3,979.87",
# 		 "$349.89",
# 		 "$158.38",
# 		 "$494.10",
# 		 "$902.35",
# 		 "$579.06"
# 	],
# [
# 		 "Morgan Gallegos",
# 		 "eget.varius@outlook.com",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$28,410.10",
# 		 "$3,298.86",
# 		 "$124.96",
# 		 "$250.87",
# 		 "$350.01",
# 		 "$337.26",
# 		 "$400.66"
# 	],
# [
# 		 "Aphrodite York",
# 		 "eu.accumsan@hotmail.org",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$90,723.12",
# 		 "$2,925.65",
# 		 "$173.02",
# 		 "$53.85",
# 		 "$818.60",
# 		 "$896.16",
# 		 "$754.49"
# 	],
# [
# 		 "Claudia Carrillo",
# 		 "amet.faucibus@aol.couk",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$83,315.82",
# 		 "$3,265.18",
# 		 "$477.64",
# 		 "$246.01",
# 		 "$602.07",
# 		 "$874.20",
# 		 "$9.15"
# 	],
# [
# 		 "Tatum Franks",
# 		 "accumsan.convallis@hotmail.org",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$153,490.24",
# 		 "$934.53",
# 		 "$227.20",
# 		 "$43.10",
# 		 "$110.64",
# 		 "$727.02",
# 		 "$520.37"
# 	],
# [
# 		 "Rajah Mcneil",
# 		 "quisque.libero@hotmail.org",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$24,684.20",
# 		 "$1,420.23",
# 		 "$320.13",
# 		 "$132.28",
# 		 "$486.70",
# 		 "$597.15",
# 		 "$735.28"
# 	],
# [
# 		 "Barclay Vinson",
# 		 "malesuada.malesuada.integer@protonmail.org",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$71,043.54",
# 		 "$1,946.58",
# 		 "$458.50",
# 		 "$130.36",
# 		 "$704.40",
# 		 "$199.98",
# 		 "$960.77"
# 	],
# [
# 		 "Robert Olson",
# 		 "dolor.vitae@icloud.edu",
# 		 "Ontario",
# 		 "Canada",
# 		 "$51,282.48",
# 		 "$2,467.25",
# 		 "$353.44",
# 		 "$272.80",
# 		 "$105.91",
# 		 "$232.37",
# 		 "$745.47"
# 	],
# [
# 		 "Tatyana Mosley",
# 		 "cras.interdum@aol.edu",
# 		 "Alberta",
# 		 "Canada",
# 		 "$143,526.85",
# 		 "$690.34",
# 		 "$473.08",
# 		 "$104.51",
# 		 "$101.78",
# 		 "$398.51",
# 		 "$954.07"
# 	],
# [
# 		 "Freya Webster",
# 		 "quisque@aol.ca",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$161,437.82",
# 		 "$3,342.78",
# 		 "$192.41",
# 		 "$191.46",
# 		 "$692.46",
# 		 "$588.67",
# 		 "$33.19"
# 	],
# [
# 		 "Ulla Shannon",
# 		 "nunc.quis@hotmail.edu",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$169,058.22",
# 		 "$1,784.43",
# 		 "$147.56",
# 		 "$58.97",
# 		 "$132.48",
# 		 "$174.76",
# 		 "$831.29"
# 	],
# [
# 		 "Grant Hurley",
# 		 "sit.amet@icloud.com",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$98,064.84",
# 		 "$2,807.58",
# 		 "$282.07",
# 		 "$93.94",
# 		 "$98.46",
# 		 "$840.84",
# 		 "$912.74"
# 	],
# [
# 		 "Tucker Clay",
# 		 "magna.phasellus@yahoo.org",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$50,259.53",
# 		 "$2,765.89",
# 		 "$153.72",
# 		 "$116.41",
# 		 "$50.99",
# 		 "$493.10",
# 		 "$102.65"
# 	],
# [
# 		 "Petra Brooks",
# 		 "ullamcorper.duis@google.edu",
# 		 "Ontario",
# 		 "Canada",
# 		 "$68,265.23",
# 		 "$4,408.49",
# 		 "$214.49",
# 		 "$252.49",
# 		 "$337.17",
# 		 "$252.83",
# 		 "$632.54"
# 	],
# [
# 		 "Nathaniel Bartlett",
# 		 "ac.mattis@aol.org",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$106,999.50",
# 		 "$2,743.50",
# 		 "$196.01",
# 		 "$171.42",
# 		 "$663.15",
# 		 "$928.72",
# 		 "$24.91"
# 	],
# [
# 		 "Phyllis Strickland",
# 		 "non.egestas@aol.edu",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$131,856.58",
# 		 "$3,640.13",
# 		 "$281.09",
# 		 "$242.29",
# 		 "$421.02",
# 		 "$654.24",
# 		 "$477.89"
# 	],
# [
# 		 "Asher Holland",
# 		 "odio.nam@outlook.org",
# 		 "Alberta",
# 		 "Canada",
# 		 "$152,293.25",
# 		 "$3,819.56",
# 		 "$296.97",
# 		 "$110.24",
# 		 "$675.30",
# 		 "$326.32",
# 		 "$295.17"
# 	],
# [
# 		 "Porter Barry",
# 		 "egestas.ligula@protonmail.ca",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$102,418.69",
# 		 "$3,141.30",
# 		 "$327.74",
# 		 "$205.40",
# 		 "$156.35",
# 		 "$742.45",
# 		 "$135.69"
# 	],
# [
# 		 "Justin Mosley",
# 		 "donec.consectetuer.mauris@icloud.net",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$20,450.21",
# 		 "$1,274.47",
# 		 "$260.89",
# 		 "$197.39",
# 		 "$366.59",
# 		 "$537.02",
# 		 "$380.88"
# 	],
# [
# 		 "Jesse Mckee",
# 		 "nibh.vulputate.mauris@aol.org",
# 		 "Alberta",
# 		 "Canada",
# 		 "$99,815.38",
# 		 "$2,299.13",
# 		 "$437.38",
# 		 "$279.94",
# 		 "$377.61",
# 		 "$480.17",
# 		 "$237.09"
# 	],
# [
# 		 "Xaviera Skinner",
# 		 "sed.eu.eros@yahoo.edu",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$150,038.35",
# 		 "$3,517.12",
# 		 "$499.52",
# 		 "$85.56",
# 		 "$21.95",
# 		 "$935.76",
# 		 "$66.18"
# 	],
# [
# 		 "Carson Campbell",
# 		 "facilisis.eget@outlook.com",
# 		 "Ontario",
# 		 "Canada",
# 		 "$161,902.45",
# 		 "$3,163.79",
# 		 "$125.01",
# 		 "$212.04",
# 		 "$239.31",
# 		 "$331.17",
# 		 "$426.71"
# 	],
# [
# 		 "Selma Phillips",
# 		 "est@icloud.edu",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$154,682.06",
# 		 "$3,623.19",
# 		 "$425.44",
# 		 "$28.14",
# 		 "$81.94",
# 		 "$984.77",
# 		 "$121.61"
# 	],
# [
# 		 "Clarke Cardenas",
# 		 "sed.eu@yahoo.ca",
# 		 "Quebec",
# 		 "Canada",
# 		 "$112,455.49",
# 		 "$3,426.01",
# 		 "$381.59",
# 		 "$266.58",
# 		 "$968.03",
# 		 "$568.99",
# 		 "$64.43"
# 	],
# [
# 		 "Jackson Mayo",
# 		 "sed@hotmail.net",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$36,078.18",
# 		 "$2,454.62",
# 		 "$364.30",
# 		 "$187.16",
# 		 "$846.04",
# 		 "$851.35",
# 		 "$338.11"
# 	],
# [
# 		 "Isabelle Richardson",
# 		 "aliquet.magna@protonmail.com",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$66,626.05",
# 		 "$4,348.74",
# 		 "$218.11",
# 		 "$243.74",
# 		 "$533.85",
# 		 "$720.58",
# 		 "$184.53"
# 	],
# [
# 		 "Ulla Jefferson",
# 		 "orci.lobortis@yahoo.couk",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$73,018.03",
# 		 "$3,415.65",
# 		 "$360.37",
# 		 "$197.73",
# 		 "$102.67",
# 		 "$961.09",
# 		 "$329.25"
# 	],
# [
# 		 "Lucy Mitchell",
# 		 "quis.urna.nunc@aol.com",
# 		 "Alberta",
# 		 "Canada",
# 		 "$77,290.45",
# 		 "$4,672.62",
# 		 "$324.46",
# 		 "$62.54",
# 		 "$196.25",
# 		 "$761.71",
# 		 "$29.51"
# 	],
# [
# 		 "Ciaran Hunt",
# 		 "integer@yahoo.net",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$107,478.24",
# 		 "$723.10",
# 		 "$247.56",
# 		 "$290.78",
# 		 "$766.03",
# 		 "$609.54",
# 		 "$413.18"
# 	],
# [
# 		 "Amery Mueller",
# 		 "faucibus@hotmail.couk",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$98,741.54",
# 		 "$3,249.35",
# 		 "$322.01",
# 		 "$213.55",
# 		 "$104.02",
# 		 "$335.08",
# 		 "$706.41"
# 	],
# [
# 		 "Amelia Ruiz",
# 		 "mi.tempor@outlook.net",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$67,481.28",
# 		 "$3,471.40",
# 		 "$395.13",
# 		 "$67.45",
# 		 "$309.33",
# 		 "$420.37",
# 		 "$273.37"
# 	],
# [
# 		 "Brandon Stephens",
# 		 "vitae.risus@yahoo.com",
# 		 "Yukon",
# 		 "Canada",
# 		 "$172,150.02",
# 		 "$1,999.43",
# 		 "$101.42",
# 		 "$154.44",
# 		 "$355.06",
# 		 "$903.76",
# 		 "$59.39"
# 	],
# [
# 		 "Avye Tate",
# 		 "consectetuer.rhoncus@aol.edu",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$179,391.58",
# 		 "$897.64",
# 		 "$386.06",
# 		 "$31.23",
# 		 "$781.07",
# 		 "$724.74",
# 		 "$949.99"
# 	],
# [
# 		 "Stacy Hood",
# 		 "velit.justo@icloud.net",
# 		 "Ontario",
# 		 "Canada",
# 		 "$110,061.60",
# 		 "$974.91",
# 		 "$423.03",
# 		 "$247.49",
# 		 "$34.56",
# 		 "$560.21",
# 		 "$444.69"
# 	],
# [
# 		 "Deborah Vasquez",
# 		 "tempus.lorem.fringilla@aol.org",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$48,856.47",
# 		 "$1,278.73",
# 		 "$276.45",
# 		 "$85.95",
# 		 "$36.87",
# 		 "$912.97",
# 		 "$452.67"
# 	],
# [
# 		 "Griffin Suarez",
# 		 "sed.sapien@outlook.com",
# 		 "Prince Edward Island",
# 		 "Canada",
# 		 "$27,152.93",
# 		 "$3,580.02",
# 		 "$214.28",
# 		 "$258.45",
# 		 "$446.75",
# 		 "$647.00",
# 		 "$289.64"
# 	],
# [
# 		 "Sybill Foley",
# 		 "arcu.sed@hotmail.com",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$162,724.31",
# 		 "$2,070.12",
# 		 "$421.64",
# 		 "$232.17",
# 		 "$276.41",
# 		 "$552.96",
# 		 "$463.21"
# 	],
# [
# 		 "Denton Bentley",
# 		 "eu.dui@hotmail.ca",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$25,857.43",
# 		 "$4,295.01",
# 		 "$152.84",
# 		 "$239.54",
# 		 "$430.60",
# 		 "$446.48",
# 		 "$39.09"
# 	],
# [
# 		 "Phillip Steele",
# 		 "nunc@yahoo.net",
# 		 "Alberta",
# 		 "Canada",
# 		 "$168,466.58",
# 		 "$812.39",
# 		 "$246.24",
# 		 "$258.58",
# 		 "$716.95",
# 		 "$741.87",
# 		 "$473.82"
# 	],
# [
# 		 "Xavier Bell",
# 		 "orci.adipiscing@hotmail.couk",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$66,598.12",
# 		 "$2,293.46",
# 		 "$242.59",
# 		 "$104.79",
# 		 "$59.35",
# 		 "$235.20",
# 		 "$682.09"
# 	],
# [
# 		 "Baxter Shepherd",
# 		 "et@hotmail.couk",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$170,904.97",
# 		 "$1,904.30",
# 		 "$366.59",
# 		 "$240.77",
# 		 "$304.90",
# 		 "$517.27",
# 		 "$877.61"
# 	],
# [
# 		 "Jermaine Farmer",
# 		 "faucibus.leo@google.ca",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$74,401.28",
# 		 "$4,004.72",
# 		 "$400.58",
# 		 "$183.12",
# 		 "$934.98",
# 		 "$581.79",
# 		 "$145.31"
# 	],
# [
# 		 "Orla Bean",
# 		 "tempus.lorem@yahoo.ca",
# 		 "Ontario",
# 		 "Canada",
# 		 "$66,536.71",
# 		 "$1,783.92",
# 		 "$272.18",
# 		 "$201.89",
# 		 "$424.80",
# 		 "$631.76",
# 		 "$538.68"
# 	],
# [
# 		 "Karen Jensen",
# 		 "quisque.fringilla@aol.net",
# 		 "Saskatchewan",
# 		 "Canada",
# 		 "$123,181.99",
# 		 "$3,524.61",
# 		 "$267.39",
# 		 "$252.46",
# 		 "$132.90",
# 		 "$688.34",
# 		 "$582.84"
# 	],
# [
# 		 "Hamish Garner",
# 		 "tortor.at@outlook.ca",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$71,530.86",
# 		 "$588.77",
# 		 "$328.06",
# 		 "$28.63",
# 		 "$812.37",
# 		 "$421.80",
# 		 "$350.53"
# 	],
# [
# 		 "Jarrod Miles",
# 		 "volutpat@google.org",
# 		 "Nunavut",
# 		 "Canada",
# 		 "$49,749.00",
# 		 "$3,960.54",
# 		 "$130.13",
# 		 "$100.58",
# 		 "$828.79",
# 		 "$184.07",
# 		 "$605.57"
# 	],
# [
# 		 "Macey Randall",
# 		 "feugiat.metus@hotmail.org",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$32,920.33",
# 		 "$4,484.77",
# 		 "$428.54",
# 		 "$79.55",
# 		 "$465.15",
# 		 "$532.11",
# 		 "$386.82"
# 	],
# [
# 		 "Xandra Ferrell",
# 		 "lorem.ipsum.sodales@hotmail.couk",
# 		 "Quebec",
# 		 "Canada",
# 		 "$161,003.23",
# 		 "$978.96",
# 		 "$345.16",
# 		 "$138.37",
# 		 "$405.26",
# 		 "$619.02",
# 		 "$751.89"
# 	],
# [
# 		 "Trevor Stephenson",
# 		 "quis@yahoo.ca",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$81,304.67",
# 		 "$3,129.91",
# 		 "$297.30",
# 		 "$195.95",
# 		 "$17.91",
# 		 "$987.80",
# 		 "$658.03"
# 	],
# [
# 		 "Rose Walters",
# 		 "facilisis.suspendisse.commodo@aol.com",
# 		 "Quebec",
# 		 "Canada",
# 		 "$138,409.88",
# 		 "$3,110.79",
# 		 "$327.63",
# 		 "$49.54",
# 		 "$754.43",
# 		 "$506.91",
# 		 "$626.56"
# 	],
# [
# 		 "Wylie Mcdonald",
# 		 "sed@outlook.edu",
# 		 "Ontario",
# 		 "Canada",
# 		 "$96,768.66",
# 		 "$1,974.22",
# 		 "$219.32",
# 		 "$152.60",
# 		 "$538.28",
# 		 "$363.83",
# 		 "$976.82"
# 	],
# [
# 		 "Quin Sampson",
# 		 "sapien.molestie@protonmail.net",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$67,349.20",
# 		 "$4,849.63",
# 		 "$153.33",
# 		 "$182.63",
# 		 "$7.38",
# 		 "$763.95",
# 		 "$409.77"
# 	],
# [
# 		 "Wesley Carroll",
# 		 "ipsum.donec@hotmail.ca",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$155,396.00",
# 		 "$829.88",
# 		 "$499.50",
# 		 "$210.95",
# 		 "$563.24",
# 		 "$655.00",
# 		 "$224.19"
# 	],
# [
# 		 "Myles Bradford",
# 		 "cursus.in.hendrerit@aol.ca",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$69,105.97",
# 		 "$2,351.65",
# 		 "$475.63",
# 		 "$211.43",
# 		 "$979.15",
# 		 "$366.25",
# 		 "$952.03"
# 	],
# [
# 		 "Ina Kerr",
# 		 "quisque.varius@yahoo.couk",
# 		 "Quebec",
# 		 "Canada",
# 		 "$144,715.72",
# 		 "$1,600.19",
# 		 "$290.33",
# 		 "$134.68",
# 		 "$964.47",
# 		 "$352.05",
# 		 "$692.09"
# 	],
# [
# 		 "Lael Flowers",
# 		 "nulla.donec@outlook.com",
# 		 "Quebec",
# 		 "Canada",
# 		 "$121,684.59",
# 		 "$2,530.04",
# 		 "$112.64",
# 		 "$38.90",
# 		 "$965.45",
# 		 "$492.15",
# 		 "$142.01"
# 	],
# [
# 		 "Paula Hawkins",
# 		 "diam.duis.mi@hotmail.com",
# 		 "New Brunswick",
# 		 "Canada",
# 		 "$20,134.49",
# 		 "$3,952.72",
# 		 "$424.05",
# 		 "$20.70",
# 		 "$837.34",
# 		 "$442.66",
# 		 "$811.70"
# 	],
# [
# 		 "Tasha Melton",
# 		 "sem.consequat@google.edu",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$51,691.07",
# 		 "$1,822.37",
# 		 "$458.77",
# 		 "$105.98",
# 		 "$818.59",
# 		 "$661.93",
# 		 "$680.51"
# 	],
# [
# 		 "Lavinia House",
# 		 "ut.semper@hotmail.edu",
# 		 "Prince Edward Island",
# 		 "Canada",
# 		 "$97,286.40",
# 		 "$2,242.52",
# 		 "$136.26",
# 		 "$233.15",
# 		 "$205.43",
# 		 "$156.43",
# 		 "$251.79"
# 	],
# [
# 		 "Talon Sparks",
# 		 "consectetuer.rhoncus@icloud.ca",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$46,745.71",
# 		 "$4,627.73",
# 		 "$289.09",
# 		 "$21.35",
# 		 "$206.14",
# 		 "$268.73",
# 		 "$853.48"
# 	],
# [
# 		 "Ray Sweet",
# 		 "mauris.integer@protonmail.couk",
# 		 "British Columbia",
# 		 "Canada",
# 		 "$45,261.46",
# 		 "$1,491.01",
# 		 "$318.98",
# 		 "$223.33",
# 		 "$243.00",
# 		 "$265.06",
# 		 "$562.55"
# 	],
# [
# 		 "Kimberley Walter",
# 		 "suspendisse@yahoo.org",
# 		 "Newfoundland and Labrador",
# 		 "Canada",
# 		 "$138,550.85",
# 		 "$2,543.51",
# 		 "$416.85",
# 		 "$218.77",
# 		 "$116.40",
# 		 "$539.98",
# 		 "$602.59"
# 	],
# [
# 		 "Kuame Vaughan",
# 		 "ullamcorper@google.com",
# 		 "Nova Scotia",
# 		 "Canada",
# 		 "$122,498.08",
# 		 "$833.89",
# 		 "$162.96",
# 		 "$143.13",
# 		 "$184.40",
# 		 "$710.24",
# 		 "$550.99"
# 	],
# [
# 		 "Tanner Grimes",
# 		 "urna.convallis.erat@protonmail.couk",
# 		 "Northwest Territories",
# 		 "Canada",
# 		 "$117,863.78",
# 		 "$513.50",
# 		 "$464.94",
# 		 "$230.36",
# 		 "$804.04",
# 		 "$602.91",
# 		 "$580.68"
# 	],
# [
# 		 "Nerea Barrett",
# 		 "nunc@outlook.com",
# 		 "Manitoba",
# 		 "Canada",
# 		 "$69,174.18",
# 		 "$4,234.07",
# 		 "$202.93",
# 		 "$231.50",
# 		 "$926.91",
# 		 "$476.83",
# 		 "$499.10"
# 	]
]


grocery20 = []
grocery40 = []
grocery50 = []
grocery70 = []
grocery90 = []

cell20 = []
cell40 = []
cell50 = []
cell70 = []
cell90 = []

liabilities20 = []
liabilities40 = []
liabilities50 = []
liabilities70 = []
liabilities90 = []

housing20 = []
housing40 = []
housing50 = []
housing70 = []
housing90 = []


def remove_comma(cost):
	cost = cost.replace(',', '')
	cost = cost.replace('$', '')
	cost = float(cost)
	return int(cost)


def data_to_dict():
	for person in data:

		if remove_comma(person[4]) <= 40000:
			housing20.append(remove_comma(person[5]))
			grocery20.append(remove_comma(person[6]))
			cell20.append(remove_comma(person[7]))
			liabilities20.append(remove_comma(person[9]))

		elif remove_comma(person[4]) <= 50000:
			housing40.append(remove_comma(person[5]))
			grocery40.append(remove_comma(person[6]))
			cell40.append(remove_comma(person[7]))
			liabilities40.append(remove_comma(person[9]))

		elif remove_comma(person[4]) <= 70000:
			housing50.append(remove_comma(person[5]))
			grocery50.append(remove_comma(person[6]))
			cell50.append(remove_comma(person[7]))
			liabilities50.append(remove_comma(person[9]))

		elif remove_comma(person[4]) <= 90000:
			housing70.append(remove_comma(person[5]))
			grocery70.append(remove_comma(person[6]))
			cell70.append(remove_comma(person[7]))
			liabilities70.append(remove_comma(person[9]))

		else:
			housing90.append(remove_comma(person[5]))
			grocery90.append(remove_comma(person[6]))
			cell90.append(remove_comma(person[7]))
			liabilities90.append(remove_comma(person[9]))


def compare_data(person=["Graham", "graham@gmail.com", "Ontario", "90000", "1500", "300", "50", "0", "1500", "1000"]):
	text = ""

	if int(person[3]) <= 40000:
		lower_bound = np.percentile(grocery20, 25)
		upper_bound = np.percentile(grocery20, 75)
		if int(person[5]) < lower_bound or int(person[5]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on groceries for people in the income range 20-40 thousand."
			if int(person[5]) > upper_bound:
				text += " Consider spending less on groceries."

		lower_bound = np.percentile(cell20, 25)
		upper_bound = np.percentile(cell20, 75)
		if int(person[6]) < lower_bound or int(person[6]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on your cell phone for people in the income range 20-40 thousand."
			if int(person[6]) > upper_bound:
				text += " Consider spending less on your phone."

		lower_bound = np.percentile(liabilities20, 25)
		upper_bound = np.percentile(liabilities20, 75)
		if int(person[9]) < lower_bound or int(person[9]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on liabilities for people in the income range 20-40 thousand."
			if int(person[9]) > upper_bound:
				text += " Consider spending less on your liabilities."

		lower_bound = np.percentile(housing20, 25)
		upper_bound = np.percentile(housing20, 75)
		if int(person[4]) < lower_bound or int(person[4]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on housing for people in the income range 20-40 thousand."
			if int(person[4]) > upper_bound:
				text += " Consider spending less on housing."

	elif int(person[3]) <= 50000:
		lower_bound = np.percentile(grocery40, 25)
		upper_bound = np.percentile(grocery40, 75)
		if int(person[5]) < lower_bound or int(person[5]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on groceries for people in the income range 40-50 thousand."
			if int(person[5]) > upper_bound:
				text += " Consider spending less on groceries."

		lower_bound = np.percentile(cell40, 25)
		upper_bound = np.percentile(cell40, 75)
		if int(person[6]) < lower_bound or int(person[6]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on your cell phone for people in the income range 40-50 thousand."
			if int(person[6]) > upper_bound:
				text += " Consider spending less on your phone."

		lower_bound = np.percentile(liabilities40, 25)
		upper_bound = np.percentile(liabilities40, 75)
		if int(person[9]) < lower_bound or int(person[9]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on liabilities for people in the income range 40-50 thousand."
			if int(person[9]) > upper_bound:
				text += " Consider spending less on liabilities."

		lower_bound = np.percentile(housing40, 25)
		upper_bound = np.percentile(housing40, 75)
		if int(person[4]) < lower_bound or int(person[4]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on housing for people in the income range 40-50 thousand."
			if int(person[4]) > upper_bound:
				text += " Consider spending less on housing."

	elif int(person[3]) <= 70000:
		lower_bound = np.percentile(grocery50, 25)
		upper_bound = np.percentile(grocery50, 75)
		if int(person[5]) < lower_bound or int(person[5]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on groceries for people in the income range 50-70 thousand."
			if int(person[5]) > upper_bound:
				text += " Consider spending less on groceries."

		lower_bound = np.percentile(cell50, 25)
		upper_bound = np.percentile(cell50, 75)
		if int(person[6]) < lower_bound or int(person[6]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on your cell phone for people in the income range 50-70 thousand."
			if int(person[6]) > upper_bound:
				text += " Consider spending less on your phone."

		lower_bound = np.percentile(liabilities50, 25)
		upper_bound = np.percentile(liabilities50, 75)
		if int(person[9]) < lower_bound or int(person[9]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on liabilities for people in the income range 50-70 thousand."
			if int(person[9]) > upper_bound:
				text += " Consider spending less on liabilities."

		lower_bound = np.percentile(housing50, 25)
		upper_bound = np.percentile(housing50, 75)
		if int(person[4]) < lower_bound or int(person[4]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on housing for people in the income range 50-70 thousand."
			if int(person[4]) > upper_bound:
				text += " Consider spending less on housing."

	elif int(person[3]) <= 90000:
		lower_bound = np.percentile(grocery70, 25)
		upper_bound = np.percentile(grocery70, 75)
		if int(person[5]) < lower_bound or int(person[5]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on groceries for people in the income range 70-90 thousand."
			if int(person[5]) > upper_bound:
				text += " Consider spending less on groceries."

		lower_bound = np.percentile(cell70, 25)
		upper_bound = np.percentile(cell70, 75)
		if int(person[6]) < lower_bound or int(person[6]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on your cell phone for people in the income range 70-90 thousand."
			if int(person[6]) > upper_bound:
				text += " Consider spending less on your phone."

		lower_bound = np.percentile(liabilities70, 25)
		upper_bound = np.percentile(liabilities70, 75)
		if int(person[9]) < lower_bound or int(person[9]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on liabilities for people in the income range 70-90 thousand."
			if int(person[9]) > upper_bound:
				text += " Consider spending less on liabilities."

		lower_bound = np.percentile(housing70, 25)
		upper_bound = np.percentile(housing70, 75)
		if int(person[4]) < lower_bound or int(person[4]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on housing for people in the income range 70-90 thousand."
			if int(person[4]) > upper_bound:
				text += " Consider spending less on housing."

	else:
		lower_bound = np.percentile(grocery90, 25)
		upper_bound = np.percentile(grocery90, 75)
		if int(person[5]) < lower_bound or int(person[5]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on groceries for people in the income range 90 thousand plus."
			if int(person[5]) > upper_bound:
				text += " Consider spending less on groceries."

		lower_bound = np.percentile(cell90, 25)
		upper_bound = np.percentile(cell90, 75)
		if int(person[6]) < lower_bound or int(person[6]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on your cell phone for people in the income range 90 thousand plus."
			if int(person[6]) > upper_bound:
				text += " Consider spending less on your phone."

		lower_bound = np.percentile(liabilities90, 25)
		upper_bound = np.percentile(liabilities90, 75)
		if int(person[9]) < lower_bound or int(person[9]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on liabilities for people in the income range 90 thousand plus."
			if int(person[9]) > upper_bound:
				text += " Consider spending less on liabilities."

		lower_bound = np.percentile(housing90, 25)
		upper_bound = np.percentile(housing90, 75)
		if int(person[4]) < lower_bound or int(person[4]) > upper_bound:
			text += "\n\nYou are an outlier for the amount that you spend on housing for people in the income range 90 thousand plus."
			if int(person[4]) > upper_bound:
				text += " Consider spending less on housing."

	suggest_investment(person, text)


def send_email(person, text):
	subject = person[0] + "'s Financial Report"  # create a string that is the subject
	emailText = 'Subject: {}\n\n{}'.format(subject, text)  # set the subject of emailText to the subjec above

	sender, password = 'grahamTestMaker@gmail.com', 'TestMakePassword1'  # t #the sender username then password MUST GMAIL ACCOUNT, dont hack me pls :)
	recieve = person[1]  # define the reciever...
	message = emailText  # the message
	port = 465  # standard ssl port - router could block ssl port

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:  # access the gmail server
		server.login(sender, password)  # login to gmail account
		server.sendmail(sender, recieve, message)  # send mail


def convert_input(user_input):
	user_list = []
	next_string = ""
	user_input = user_input.replace('[', '')
	user_input = user_input.replace(']', '')

	for i in range(len(user_input)):
		char = user_input[i]
		if char != ',':
			next_string += char
		else:
			user_list.append(next_string)
			next_string = ""

	return user_list
			

def suggest_investment(person, text):
	income = person[3]
	house_costs = person[4]
	grocery_costs = person[5]
	phone_costs = person[6]
	insurance_costs = person[8]
	liability_costs = person[9]

	monthly_costs = 12 * (house_costs + grocery_costs + phone_costs + insurance_costs + liability_costs)
	extra_money = income - monthly_costs

	text += '\n\nYou will have $' + str(extra_money) + 'extra at the end of the year with your current financial situation.'
	text += '\nOur financial advisors recommend investing that money.'

	if extra_money < 10000:
		text += '\n\tWith your current money, investing in _ will be the best use of your finances.'
		text += '\n\tThis is because _.'
		text += '\n\tThere is _ risk associated with this type of investment.'

	elif extra_money < 20000:
		text += '\n\tWith your current money, investing in _ will be the best use of your finances.'
		text += '\n\tThis is because _.'
		text += '\n\tThere is _ risk associated with this type of investment.'

	elif extra_money < 30000:
		text += '\n\tWith your current money, investing in _ will be the best use of your finances.'
		text += '\n\tThis is because _.'
		text += '\n\tThere is _ risk associated with this type of investment.'

	# mutual funds = very safe and low risk. 
	# real estate = good if you have a lot of money and are willing to manage it or pay someone else to manage it
	# hedge funds = requires research on your part
	# preferred shares = 

	send_email(person, text)




def main(input):

	person = convert_input(input)

	# Organizes data into each data set for different income ranges.
	data_to_dict()
	compare_data(person)
	suggest_investment(person)


from flask import Flask, request


app = Flask(__name__)

@app.route("/graham")
def graham():
	input = (request.args["arr"])
	main(input)
	return "mail sent!"

app.run(host='0.0.0.0', port=5432)
