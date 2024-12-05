@echo off
setlocal enabledelayedexpansion

:: Data definition for all 50 states with additional information
set "states[0]=Alabama|Montgomery|Camellia|Yellowhammer|1819|9|22"
set "states[1]=Alaska|Juneau|Forget-me-not|Willow Ptarmigan|1959|3|49"
set "states[2]=Arizona|Phoenix|Saguaro Cactus Blossom|Cactus Wren|1912|11|48"
set "states[3]=Arkansas|Little Rock|Apple Blossom|Northern Mockingbird|1836|6|25"
set "states[4]=California|Sacramento|California Poppy|California Quail|1850|54|31"
set "states[5]=Colorado|Denver|Rocky Mountain Columbine|Lark Bunting|1876|10|38"
set "states[6]=Connecticut|Hartford|Mountain Laurel|American Robin|1788|7|5"
set "states[7]=Delaware|Dover|Peach Blossom|Delaware Blue Hen|1787|3|1"
set "states[8]=Florida|Tallahassee|Orange Blossom|Northern Mockingbird|1845|30|27"
set "states[9]=Georgia|Atlanta|Cherokee Rose|Brown Thrasher|1788|16|4"
set "states[10]=Hawaii|Honolulu|Hibiscus|Nene|1959|4|50"
set "states[11]=Idaho|Boise|Syringa|Mountain Bluebird|1890|4|43"
set "states[12]=Illinois|Springfield|Violet|Northern Cardinal|1818|19|21"
set "states[13]=Indiana|Indianapolis|Peony|Northern Cardinal|1816|11|19"
set "states[14]=Iowa|Des Moines|Wild Prairie Rose|Eastern Goldfinch|1846|6|29"
set "states[15]=Kansas|Topeka|Sunflower|Western Meadowlark|1861|6|34"
set "states[16]=Kentucky|Frankfort|Goldenrod|Northern Cardinal|1792|8|15"
set "states[17]=Louisiana|Baton Rouge|Magnolia|Brown Pelican|1812|8|18"
set "states[18]=Maine|Augusta|White Pine Cone and Tassel|Chickadee|1820|4|23"
set "states[19]=Maryland|Annapolis|Black-Eyed Susan|Baltimore Oriole|1788|10|7"
set "states[20]=Massachusetts|Boston|Mayflower|Black-Capped Chickadee|1788|11|6"
set "states[21]=Michigan|Lansing|Apple Blossom|American Robin|1837|15|26"
set "states[22]=Minnesota|Saint Paul|Pink and White Lady's Slipper|Common Loon|1858|10|32"
set "states[23]=Mississippi|Jackson|Magnolia|Northern Mockingbird|1817|6|20"
set "states[24]=Missouri|Jefferson City|Hawthorn|Eastern Bluebird|1821|10|24"
set "states[25]=Montana|Helena|Bitterroot|Western Meadowlark|1889|3|41"
set "states[26]=Nebraska|Lincoln|Goldenrod|Western Meadowlark|1867|5|37"
set "states[27]=Nevada|Carson City|Sagebrush|Mountain Bluebird|1864|6|36"
set "states[28]=New Hampshire|Concord|Purple Lilac|Purple Finch|1788|4|9"
set "states[29]=New Jersey|Trenton|Violet|Eastern Goldfinch|1787|14|3"
set "states[30]=New Mexico|Santa Fe|Yucca Flower|Greater Roadrunner|1912|5|47"
set "states[31]=New York|Albany|Rose|Eastern Bluebird|1788|28|11"
set "states[32]=North Carolina|Raleigh|Flowering Dogwood|Northern Cardinal|1789|16|12"
set "states[33]=North Dakota|Bismarck|Wild Prairie Rose|Western Meadowlark|1889|3|39"
set "states[34]=Ohio|Columbus|Scarlet Carnation|Northern Cardinal|1803|17|17"
set "states[35]=Oklahoma|Oklahoma City|Mistletoe|Scissor-tailed Flycatcher|1907|7|46"
set "states[36]=Oregon|Salem|Oregon Grape|Western Meadowlark|1859|8|33"
set "states[37]=Pennsylvania|Harrisburg|Mountain Laurel|Ruffed Grouse|1787|19|2"
set "states[38]=Rhode Island|Providence|Violet|Rhode Island Red|1790|4|13"
set "states[39]=South Carolina|Columbia|Yellow Jessamine|Carolina Wren|1788|9|8"
set "states[40]=South Dakota|Pierre|Pasque Flower|Ring-necked Pheasant|1889|3|40"
set "states[41]=Tennessee|Nashville|Iris|Northern Mockingbird|1796|11|16"
set "states[42]=Texas|Austin|Bluebonnet|Northern Mockingbird|1845|40|28"
set "states[43]=Utah|Salt Lake City|Sego Lily|California Gull|1896|6|45"
set "states[44]=Vermont|Montpelier|Red Clover|Hermit Thrush|1791|3|14"
set "states[45]=Virginia|Richmond|American Dogwood|Northern Cardinal|1788|13|10"
set "states[46]=Washington|Olympia|Rhododendron|Willow Goldfinch|1889|12|42"
set "states[47]=West Virginia|Charleston|Rhododendron|Northern Cardinal|1863|4|35"
set "states[48]=Wisconsin|Madison|Wood Violet|American Robin|1848|10|30"
set "states[49]=Wyoming|Cheyenne|Indian Paintbrush|Western Meadowlark|1890|3|44"

:: Instructions
echo Welcome to the States and Capitals Quiz!
echo You will be given 10 random questions. Try to match states with their capitals or vice versa.
echo.

:: Initialize score
set score=0

:: Loop through 10 random questions
for /L %%i in (1,1,10) do (
    set /a index=!random! %% 50
    for /f "tokens=1-7 delims=|" %%A in ("!states[!index!]!") do (
        set "state=%%A"
        set "capital=%%B"
        set "flower=%%C"
        set "bird=%%D"
        set "date_added=%%E"
        set "electoral_votes=%%F"
        set "statehood_rank=%%G"
    )

    set /a type=!random! %% 2
    if !type! equ 0 (
        echo What is the capital of !state!?
        set /p answer=Your answer: 
        if /i "!answer!"=="!capital!" (
            echo Correct!
            set /a score+=1
        ) else (
            echo Wrong! The capital of !state! is !capital!.
        )
    ) else (
        echo !capital! is the capital of which state?
        set /p answer=Your answer: 
        if /i "!answer!"=="!state!" (
            echo Correct!
            set /a score+=1
        ) else (
            echo Wrong! !capital! is the capital of !state!.
        )
    )

    :: Show detailed information about the state
    echo State: !state!
    echo  ~ Capital: !capital!
    echo  ~ Flower: !flower!
    echo  ~ Bird: !bird!
    echo  ~ Date Added: !date_added!
    echo  ~ Electoral Votes: !electoral_votes!
    echo  ~ Statehood Rank: !statehood_rank!
    echo.
)

:: Display final score
echo Your final score: !score!/10
if !score! equ 10 (
    echo Excellent! You know your states and capitals!
) else if !score! geq 7 (
    echo Good job! A little more practice and you'll master it.
) else (
    echo Keep practicing! You'll get there.
)
pause
