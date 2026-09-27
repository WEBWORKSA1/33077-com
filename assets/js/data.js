/* 33077.com — number meaning data. Readings are homophones used in Chinese culture & internet slang. */
window.DIGITS = {
  "0": { han: "零", py: "líng", sounds: [["你","nǐ","you (love-code slang)"],["灵","líng","spirit, clever"]], luck: 0, note: "Neutral. In love codes 0 stands for 你 “you” (520 = I love you). Numeric-domain traders value a leading 0 lower." },
  "1": { han: "一", py: "yī", sounds: [["要","yào","want / will"],["一","yī","one, whole, first"]], luck: 1, note: "Unity and a new start. In codes 1 often reads as 要 “want” (51 = 我要 I want)." },
  "2": { han: "二", py: "èr", sounds: [["爱","ài","love (in 520)"],["易","yì","easy"]], luck: 1, note: "“Good things come in pairs” (好事成双). In 520 it carries 爱 “love”. Beware 250 (二百五) = “idiot”." },
  "3": { han: "三", py: "sān", sounds: [["生","shēng","life, birth"],["想","xiǎng","miss / think of"],["散","sàn","split up"]], luck: 1, note: "Usually lucky: 生 “life”. In love codes 3 = 想 “miss you” (530). Lunar 3/3 is the Shangsi love festival." },
  "4": { han: "四", py: "sì", sounds: [["死","sǐ","death"],["世","shì","lifetime (in 3344)"],["是","shì","is / yes"]], luck: -3, note: "The most avoided digit: 四 sounds like 死 “death”. Buildings skip 4th floors; plates and phones with 4 sell cheaper. Exception: 3344 = 生生世世 “forever”." },
  "5": { han: "五", py: "wǔ", sounds: [["我","wǒ","I / me"],["无","wú","without"],["呜","wū","sob (555)"]], luck: 0, note: "Neutral. In codes 5 = 我 “I” (520). Linked to the Five Elements (五行)." },
  "6": { han: "六", py: "liù", sounds: [["溜","liù","smooth, skilful"],["流","liú","flow"],["禄","lù","fortune (regional)"]], luck: 2, note: "Lucky: everything goes smoothly (六六大顺). Online, 666 = “awesome, well played”." },
  "7": { han: "七", py: "qī", sounds: [["亲","qīn","kiss / dear"],["妻","qī","wife"],["起","qǐ","rise"],["气","qì","anger"],["去","qù","go / gone"]], luck: 0, note: "Mixed. Romantic in codes (770 = 亲亲你 kiss you) and the date of Qixi (7/7), but the 7th lunar month is Ghost Month and 748 is an insult." },
  "8": { han: "八", py: "bā", sounds: [["发","fā","prosper, get rich"],["拜","bài","bye (88)"],["抱","bào","hug"]], luck: 3, note: "China’s luckiest digit: 八 sounds like 发 “prosper”. The Beijing Olympics opened 8:08 pm on 8/8/2008; a Chengdu 8888-8888 phone number sold for ¥2.33M." },
  "9": { han: "九", py: "jiǔ", sounds: [["久","jiǔ","long-lasting"],["就","jiù","just / exactly"],["救","jiù","save / help"]], luck: 2, note: "Lucky: 久 “long-lasting”, prized for weddings and relationships. Historically linked to the emperor." }
};

/* category: love | life | business | fun | insult | brand */
window.CODES = [
  ["520","我爱你","wǒ ài nǐ","I love you","love","Celebrated every May 20 as “520 Day”, one of China’s busiest days for gifts and marriage registrations."],
  ["521","我愿意","wǒ yuàn yì","I do / I’m willing — also “I love you”","love","The reply to 520; May 21 is a second romantic day."],
  ["1314","一生一世","yī shēng yī shì","For a whole lifetime","love","Often paired with 520 in gift amounts, e.g. ¥1314 red packets."],
  ["5201314","我爱你一生一世","wǒ ài nǐ yī shēng yī shì","I love you for a lifetime","love","The classic long-form love code."],
  ["1314520","一生一世我爱你","yī shēng yī shì wǒ ài nǐ","All my life, I love you","love","Reverse order of 5201314."],
  ["3344","生生世世","shēng shēng shì shì","Forever, life after life","love","The one famous code where 4 is positive (世 lifetime)."],
  ["530","我想你","wǒ xiǎng nǐ","I miss you","love","3 = 想 miss, 0 = 你 you."],
  ["360","想念你","xiǎng niàn nǐ","Missing you","love",""],
  ["770","亲亲你","qīn qīn nǐ","Kiss you","love","77 = 亲亲 “kiss kiss”."],
  ["775","亲亲我","qīn qīn wǒ","Kiss me","love",""],
  ["53770","我想亲亲你","wǒ xiǎng qīn qīn nǐ","I want to kiss you","love","The closest established cousin of 33077."],
  ["7758","亲亲我吧","qīn qīn wǒ ba","Kiss me, please","love","Widely shared online; a playful request."],
  ["721","亲爱的","qīn ài de","Darling","love",""],
  ["9420","就是爱你","jiù shì ài nǐ","It’s you I love","love",""],
  ["910","就要你","jiù yào nǐ","I only want you","love",""],
  ["04551","你是我唯一","nǐ shì wǒ wéi yī","You are my one and only","love",""],
  ["1573","一往情深","yī wǎng qíng shēn","Deeply devoted","love",""],
  ["3399","长长久久","cháng cháng jiǔ jiǔ","Forever and ever","love","Popular in wedding dates and bouquet counts."],
  ["1392010","一生就爱你一个","yī shēng jiù ài nǐ yī gè","All my life I love only you","love",""],
  ["259758","爱我就娶我吧","ài wǒ jiù qǔ wǒ ba","If you love me, marry me","love",""],
  ["33077","想想你亲亲","xiǎng xiǎng nǐ qīn qīn","Thinking of you — kiss kiss","brand","A new code built from established parts (3 = 想, 0 = 你, 77 = 亲亲). It also spans China’s two love festivals, lunar 3/3 and 7/7."],
  ["33","生生 / 想想","shēng shēng","Life upon life · missing you","love","33 roses mean love for three lifetimes; lunar 3/3 is the Shangsi festival."],
  ["77","亲亲 / 七夕","qīn qīn · qī xī","Kiss kiss · Qixi festival","love","The 7th day of the 7th lunar month is Qixi, Chinese Valentine’s Day."],
  ["99","久久","jiǔ jiǔ","Long-lasting","love","99 roses = eternal love."],
  ["168","一路发","yī lù fā","Prosperity all the way","business","A favourite for shop phone numbers and prices."],
  ["518","我要发","wǒ yào fā","I will prosper","business",""],
  ["888","发发发","fā fā fā","Triple prosperity","business","Common in prices (¥888) and plates."],
  ["8888","发发发发","fā fā fā fā","Quadruple prosperity","business","Sichuan Airlines paid ¥2.33M for phone number 8888-8888 in 2003."],
  ["88","发发 / 拜拜","fā fā · bāi bāi","Double prosperity · bye-bye","business","In chat, 88 = bye-bye; in business, double fortune."],
  ["66","六六","liù liù","Smooth sailing","life",""],
  ["666","溜溜溜","liù liù liù","Awesome! Well played","fun","Gamer praise all over Chinese internet."],
  ["999","久久久","jiǔ jiǔ jiǔ","Everlasting","life",""],
  ["1414","意思意思","yì si yì si","Just a small token","life","Said when giving a modest gift or tip."],
  ["886","拜拜了","bāi bāi le","Bye then!","fun",""],
  ["233","哈哈哈","hā hā hā","LOL","fun","From emoticon #233 on the Mop forum — a laughing face."],
  ["555","呜呜呜","wū wū wū","Sob, sob","fun",""],
  ["56","无聊","wú liáo","Bored","fun",""],
  ["51","我要","wǒ yào","I want","life",""],
  ["456","是我啦","shì wǒ la","It’s me!","fun",""],
  ["484","是不是","shì bu shì","Is it or not?","fun",""],
  ["995","救救我","jiù jiù wǒ","Help me!","fun",""],
  ["7456","气死我了","qì sǐ wǒ le","I’m furious","insult","7 = 气 anger."],
  ["250","二百五","èr bǎi wǔ","Idiot","insult","Never give ¥250 as a gift."],
  ["748","去死吧","qù sǐ ba","Go die","insult","Strong insult — avoid."],
  ["0748","你去死吧","nǐ qù sǐ ba","You go die","insult","Strong insult — avoid."],
  ["14","要死","yào sǐ","“Going to die”","insult","Why plates and floors skip 14."],
  ["4","死","sǐ","Death","insult","Floors 4, 14, 24 are often missing in Chinese buildings."]
];

window.ZODIAC = [
  { n:"Rat", h:"鼠", py:"shǔ", lucky:[2,3], unlucky:[5,9], trait:"Quick-witted, resourceful, versatile" },
  { n:"Ox", h:"牛", py:"niú", lucky:[1,4], unlucky:[3], trait:"Diligent, dependable, determined" },
  { n:"Tiger", h:"虎", py:"hǔ", lucky:[1,3,4], unlucky:[6,7,8], trait:"Brave, confident, competitive" },
  { n:"Rabbit", h:"兔", py:"tù", lucky:[3,4,6], unlucky:[1,7,8], trait:"Gentle, elegant, responsible" },
  { n:"Dragon", h:"龙", py:"lóng", lucky:[1,6,7], unlucky:[3,8], trait:"Confident, ambitious, charismatic" },
  { n:"Snake", h:"蛇", py:"shé", lucky:[2,8,9], unlucky:[1,6,7], trait:"Wise, intuitive, enigmatic" },
  { n:"Horse", h:"马", py:"mǎ", lucky:[2,3,7], unlucky:[1,5,6], trait:"Energetic, independent, free-spirited" },
  { n:"Goat", h:"羊", py:"yáng", lucky:[3,4,9], unlucky:[6,7,8], trait:"Calm, gentle, creative" },
  { n:"Monkey", h:"猴", py:"hóu", lucky:[4,9], unlucky:[2,7], trait:"Clever, curious, playful" },
  { n:"Rooster", h:"鸡", py:"jī", lucky:[5,7,8], unlucky:[1,3,9], trait:"Observant, hardworking, courageous" },
  { n:"Dog", h:"狗", py:"gǒu", lucky:[3,4,9], unlucky:[1,6,7], trait:"Loyal, honest, protective" },
  { n:"Pig", h:"猪", py:"zhū", lucky:[2,5,8], unlucky:[1,7], trait:"Generous, compassionate, easy-going" }
];
window.ELEMENTS = [["Wood","木"],["Wood","木"],["Fire","火"],["Fire","火"],["Earth","土"],["Earth","土"],["Metal","金"],["Metal","金"],["Water","水"],["Water","水"]];
window.STEMS = "甲乙丙丁戊己庚辛壬癸";
window.BRANCHES = "子丑寅卯辰巳午未申酉戌亥";
