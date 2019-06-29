var stpWrds = ["a","abord","absolument","adresse", "l'adresse", "afin","ah","ai","aie","aient","aies","ailleurs","ainsi",
"ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez",
"attendu","au","aucun","aucune","aucuns","aujourd","aujourd'hui","aupres","auquel","aura","aurai","auraient","aurais",
"aurait","auras","aurez","auriez","aurions","aurons","auront","aussi","autre","autrefois","autrement","autres","autrui",
"aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avez","aviez","avions","avoir","avons","ayant",
"ayez","ayons","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","bon","boum","bravo","brrr","c","car",
"ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","celà",
"cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là",
"chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine",
"cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris",
"concernant","contre", "connais", "couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis",
"dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux",
"deuxième","deuxièmement","devant","devers","devra","devrait","different","differentes","differents","différent",
"différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse",
"diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","dos","douze","douzième",
"dring","droite","du","duquel","durant","dès","début","désormais", "d'", "e","effet","egale","egalement","egales","eh",
"elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","essai","est", "est-ce",
"et","etant","etc","etre","eu","eue","eues","euh","eurent","eus","eusse","eussent","eusses","eussiez","eussions","eut",
"eux","eux-mêmes","exactement","excepté","extenso","exterieur","eûmes","eût","eûtes","f","fais","faisaient","faisant",
"fait","faites","façon","feront","fi","flac","floc","fois","font","force","furent","fus","fusse","fussent","fusses",
"fussiez","fussions","fut","fûmes","fût","fûtes","g","gens", "grandpy", "h","ha","haut","hein","hem","hep","hi","ho",
"holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","ici","il","ils"
,"importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles",
"lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint",
"maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens",
"mille","mince","mine","minimale","moi","moi-meme","moi-même","moindres","moins","mon","mot","moyennant","multiple",
"multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement",
"neuf","neuvième","ni","nombreuses","nombreux","nommés","non","nos","notamment","notre","nous","nous-mêmes","nouveau",
"nouveaux","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf",
"ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle",
"parlent","parler","parmi","parole","parseme","partant","particulier","particulière","particulièrement","pas","passé",
"pendant","pense","permet","personne","personnes","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire",
"pièce","plein","plouf","plupart","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah",
"pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres",
"probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant",
"quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel",
"quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique",
"r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent",
"restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait", "salut", "sans","sapristi","sauf","se",
"sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","serai","seraient",
"serais","serait","seras","serez","seriez","serions","serons","seront","ses","seul","seule","seulement","si","sien",
"sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soient","sois","soit","soixante","sommes","son",
"sont","sous","souvent","soyez","soyons","specifique","specifiques","speculatif","stop","strictement","subtiles",
"suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","sujet",
"superpose","sur","surtout","t","ta","tac","tandis","tant","tardive","te","tel","telle","tellement","telles","tels",
"tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant",
"toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement",
"trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais",
"valeur","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voie","voient","voilà","vont",
"vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais",
"était","étant","état","étiez","étions","été","étée","étées","étés","êtes","être","ô", "?", "'","!","papie","papy"]
//Grandpy sentences
var beginSentence = ["Ahhhh oui c'est le ","Bien sûre mon pti c'est au ","La semaine dernière j'y étais c'est le "];
var endSentence = [" je m'ensouviens."," je suis passé devant une fois."," tu devrais y aller."]
//Begin of ajax actions
$('#spin').hide();
$(document).ready(()=> {
     $("#envoi").on('click', ()=> {
        $('#spin').show();//Start the load and set the time
         setTimeout(function () {
            $('#spin').attr('class','fas fa-spinner fa-rotate-90');
          }, 1000);
          setTimeout(function () {
            $('#spin').attr('class','fas fa-spinner fa-rotate-180');
          }, 2000);
          setTimeout(function () {
            $('#spin').attr('class','fas fa-spinner fa-rotate-270');
          }, 3000);

        var inForm = $('#inputForm').val();//Take the input value
        $('#displays').append('<li>'+ inForm +'</li>');//Add the sentence to conversations box

        //Parse the sentence about regular expression and specific words
        var regex = new RegExp('^(.)\'(.*)$');
        var parse = inForm.split(' ');
        var mainWords = [];

        parse.forEach(function(item, index, array) {
          if (stpWrds.includes(item.toLowerCase())) {
            parse.splice(index, 0);
          }
          else {
            mainWords.push(item.toLowerCase());
            console.log(mainWords);
          }
        });
            mainWords.forEach(function(item, index, array) {
            if (regex.test(item)) {
              query = regex.exec(item)[2];
            }
            else {
              query = mainWords.toString().replace(/,/g, '%20');
            }
            });

            //Start the google API and select a specific return for display address under a sentence.
            $.get(
                '/gRequest/',
                {
                query : query
                },
                displayReturnData,
                'json'
            ).fail(function() {// if the request fail
                $('#spin').hide();
                alert( "Euuuhhhh, non vraiment je ne vois pasde quoi tu parles; tu peux reformulez ?" );
                });
            function displayReturnData(reqFilter) {//If the request done read the script
                console.log(reqFilter[0].formatted_address.split(','));
                console.log(reqFilter[0].geometry.location['lat']);
                console.log(reqFilter[0].geometry.location['lng']);
                var lat = reqFilter[0].geometry.location['lat'];
                var lng = reqFilter[0].geometry.location['lng'];
                var name = reqFilter[0].name;
                addressRaw = reqFilter[0].formatted_address.split(',');
                address = addressRaw[0].replace(/\d/g, ' ');
                console.log(address);
                idSentence = Math.floor((Math.random() * 3));
                var rspGrndPy = beginSentence[idSentence]+ addressRaw +endSentence[idSentence]+'<span class="'+name+'"></span>';
                setTimeout(function () {

                    //Display the map.
                    reqRaw = 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/'+ lat +','+ lng +'/15?mapSize=500,500&pp='+ lat +','+ lng +'&key=AkuEXWHCBJkoeCzvttohvxa8Q4aVaGlvbrLfbZfb9z6Hxs-GqmAVeO0Ua9kaTGUx';
                    $('#displayMap').append('<span>'+ name +'</span><img src="'+ reqRaw +'" >');
                }, 3000);

                //Start the wiki module about the goole return and display a text.
                $.get(
                    '/wRequest/',
                    {
                    wqueryo : address
                    },
                    displaySentence,
                    'json'
                ).fail(function() {
                    $('#spin').hide();
                    alert( "J'avais une histoire sur ce quartier mais j'ai un trou de mémoire reformule moi sa plus tard." )
                });
                function displaySentence (listReturn) {
                    $('#spin').hide();// Stop the spinner
                    setTimeout(function () {
                        $('#displays').append('<li>'+ rspGrndPy +'</li>');
                        $('#displays').append('<li><a href="'+listReturn[1]+'"class="btn-social btn-outline" target="_blank"><span class="sr-only">Wikipedia</span>><i class="fab fa-wikipedia-w"></i></a><br>              _________               </li>');
                        alert("Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "
                        + listReturn[0] +"...ZZZZZZZZ Hep! GrandPy s'endort c'est l'âge pardonne moi, dis moi tous mon pti.");
                    }, 4000);
                };
            };
     });
});
