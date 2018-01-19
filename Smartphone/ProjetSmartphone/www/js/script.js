$(document).ready(function(){
                  
                  var nomPlayer="",
                  nomTeam ="",
                  urlServer = "http://localhost:8000/";
                  
                  $("#Get").click(function(){
                                  
                                  nomPlayer = $('#name').val();
                                  nomTeam = $('#team').val();
                                  alert(nomPlayer);
                                  
                                  var urlAjoutEquipe = urlServer+"?cmd=addteammember&team=" + nomTeam + "&name="+ nomPlayer;
                                  alert(urlAjoutEquipe);
                                  
                                  $.ajax({
                                         ///////////////////////////////////////////////////mettre les commentaires
                                         
                                         url: urlAjoutEquipe,
                                         
                                         type: 'GET',
                                         crossDomain: true,
                                         
                                         ContentType: "Application/text; charset=utf-8",
                                         
                                         success: function( text ) {
                                         
                                         localiserPlayer();
                                         initialize()
                                         },
                                         
                                         error: function( xhr, status, errorThrown ) {
                                         //   alert( "Sorry, there was a problem!" );
                                         console.log( "Error: " + errorThrown );
                                         console.log( "Status: " + status );
                                         console.dir( xhr );
                                         },
                                         
                                         // Code to run regardless of success or failure
                                         complete: function( xhr, status ) {
                                         //     alert( "The request is complete!" );
                                         }
                                         });
                                  
                                  
                                  });
                  ///////////////////////////////////////////////////////////////////////////
                  function localiserPlayer(){
                  
                  var urlAjoutEquipe =  serveur +"?cmd=setlocalization&team=" + nomTeam + "&name="+ nomPlayer + "&latitude=0&longitude=0";
                  $.ajax({
                         
                         url: urlAjoutEquipe,
                         
                         type: 'GET',
                         crossDomain: true,
                         
                         ContentType: "Application/text; charset=utf-8",
                         success: function( text ) {
                         
                         },
                         
                         error: function( xhr, status, errorThrown ) {
                         //   alert( "Sorry, there was a problem!" );
                         console.log( "Error: " + errorThrown );
                         console.log( "Status: " + status );
                         console.dir( xhr );
                         }
                         
                         });
                  }
                  /////////////////////////////////////////////////////////////////////////////////
                  
                  function envoiPosition(position){
                  var latitudeJoueur = position.coords.latitude;
                  var longitudeJoueur = position.coords.longitude;
                  var urlPost = serveur + "?cmd=setlocalization&team=" + nomTeam + "&name=" + nomPlayer+ "&latitude=" + latitudeJoueur + "&longitude=" + longitudeJoueur;
                  
                  alert(urlPost);
                  $.ajax({
                         url: urlPost,
                         
                         type: 'GET',
                         crossDomain: true,
                         
                         ContentType: "Application/text; charset=utf-8",
                         
                         success: function( text ) {
                         },
                         
                         error: function( xhr, status, errorThrown ) {
                         //  alert( "Sorry, there was a problem!" );
                         console.log( "Error: " + errorThrown );
                         console.log( "Status: " + status );
                         console.dir( xhr );
                         },
                         
                         // Code to run regardless of success or failure
                         complete: function( xhr, status ) {
                         }
                         });
                  }
                  
                  //////////////////////////////////////////////////////////////////////////////////
                  
                  function getPositionJoueur(equipe, name){
                  var adresseplacerjoueur = serveur + "?cmd=getteammemberlocation&team=" +equipe + "&name="+name;
                  var i = 2;
                  var latitutePositionJoueur = "";
                  var longitudePositionJoueur = "";
                  $.ajax({
                         
                         // The URL for the request
                         url: adresseplacerjoueur,
                         async : false,
                         type: 'GET',
                         crossDomain: true,
                         
                         ContentType: "Application/text; charset=utf-8",
                         
                         success: function( text3 ) {
                         
                         if(text3.charAt(1) == "N")
                         {
                         latitutePositionJoueur = 0;
                         longitudePositionJoueur = 0;
                         }
                         else
                         {
                         var resultPosition = text3;
                         while (resultPosition.charAt(i) != "'" ){
                         latitutePositionJoueur = latitutePositionJoueur + resultPosition.charAt(i);
                         i++;
                         }
                         
                         i= i+4;
                         
                         while (resultPosition.charAt(i) != "'" ){
                         longitudePositionJoueur = longitudePositionJoueur + resultPosition.charAt(i);
                         i++;
                         }
                         //$("#resultatEquipe").append(longitudePositionJoueur);
                         }},
                         
                         error: function( xhr, status, errorThrown ) {
                         //  alert( "Sorry, there was a problem!" );
                         console.log( "Error: " + errorThrown );
                         console.log( "Status: " + status );
                         console.dir( xhr );
                         },
                         // Code to run regardless of success or failure
                         complete: function( xhr, status ) {
                         //     alert( "The request is complete!" );
                         }
                         
                         });
                  
                  return {latitudePlayer: latitutePositionJoueur, longitudePlayer: longitudePositionJoueur};
                  }
                  
                  /////////////////////////////////////////////////////////////////////////
                  
                  function afficheJoueurTeam1(){
                  var adresse2 = serveur + "?cmd=listteammembers&team=equipe1";//+equipe;
                  var longitude="";
                  var latitude="";
                  var resultObj;
                  $.ajax({
                         
                         // The URL for the request
                         url: adresse2,
                         
                         type: 'GET',
                         crossDomain: true,
                         
                         ContentType: "Application/text; charset=utf-8",
                         
                         success: function( text ) {
                         
                         for (var boucle=0 ; boucle<text.length ; boucle++){
                         var nomJoueur = "";
                         var boucle2 = boucle;
                         
                         while(text.charAt(boucle2) != ","){
                         nomJoueur = nomJoueur + text.charAt(boucle2);
                         boucle2++;
                         }
                         if (nomJoueur != nomPlayer){
                         obj = getPositionJoueur("equipe1", nomJoueur);
                         if(obj.latitudePlayer != 0 && obj.longitudePlayer != 0)
                         {
                         var marker4 = new google.maps.Marker({
                                                              position: new google.maps.LatLng(obj.latitudePlayer, obj.longitudePlayer),
                                                              icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                                                              title : nomJoueur
                                                              });
                         marker4.setMap(map);
                         google.maps.event.trigger(map, 'resize');
                         }
                         var infowindow = new google.maps.InfoWindow({
                                                                     content: 'Equipe 1'
                                                                     });
                         
                         google.maps.event.addListener(marker4, 'click', function() {
                                                       infowindow.open(map, marker4);
                                                       });
                         boucle = boucle2;
                         }}
                         
                         },
                         
                         error: function( xhr, status, errorThrown ) {
                         // alert( "Oups, Erreur!" );
                         console.log( "Error: " + errorThrown );
                         console.log( "Status: " + status );
                         console.dir( xhr );
                         },
                         complete: function( xhr, status ) {
                         //     alert( "C'est bon !" );
                         }
                         
                         });
                  
                  }
                  
                  //////////////////////////////////////////////////////////////////////////
                  
                  function initialize() {
                  map = new google.maps.Map(document.getElementById("map_canvas"), {
                                            zoom: 14,
                                            center: new google.maps.LatLng(46.1666700, -1.1500000),
                                            mapTypeId: google.maps.MapTypeId.ROADMAP
                                            });
                  
                  setTimeout(envoiPosition,1000);
                  setTimeout(afficheJoueurTeam1,1000);
                  setTimeout(nextGoal,1000);
                  }
                  
                  ////////////////////////////////////////////////////////////////////////////
                  
                  function nextGoal(){
                  $.ajax({
                         
                         // The URL for the request
                         url: serveur + "?cmd=getnextgoal&team="+nomTeam,
                         
                         type: 'GET',
                         crossDomain: true,
                         
                         ContentType: "Application/text; charset=utf-8",
                         
                         success: function( text ) {
                         var resultat = text;
                         var i,j;
                         var latitudeALenvers="";
                         var latitude="";
                         var longitude="";
                         var longitudeALenvers="";
                         var premierNombre= 1;
                         
                         if(text.charAt(0) == "L" && text.charAt(1) == "e")
                         {
                         if(win == 0)
                         {
                         alert(text);
                         envoyerMessage("Bravo votre équipe a gagné");
                         envoyerMessageAgainst("LOOOSE ! Nous avons Gagné ! Bande de Loooser");
                         win = 1;
                         }
                         }
                         else
                         {
                         
                         
                         // Récupère latitude à l'envers
                         i = resultat.length;
                         while(resultat.charAt(i) != "," )
                         {
                         latitudeALenvers = latitudeALenvers + resultat.charAt(i);
                         i--;
                         }
                         
                         // Passer la virgule
                         i--;
                         // Récupère latitude à l'envers
                         while(resultat.charAt(i) != ">" ){
                         longitudeALenvers = longitudeALenvers + resultat.charAt(i);
                         i--;
                         }
                         
                         i = i-4;
                         var nomPoint="";
                         var longueurResultat = i;
                         while (i > 12 ){
                         nomPoint = nomPoint + resultat.charAt(i);
                         i--;
                         }
                         
                         // On remet à l'endroit longitude et latitude
                         for (var k=latitudeALenvers.length ; k >=0 ; k-- ){
                         latitude = latitude + latitudeALenvers.charAt(k);
                         }
                         for (var l=longitudeALenvers.length ; l >=0 ; l-- ){
                         longitude = longitude + longitudeALenvers.charAt(l);
                         }
                         // On remet à l'endroit le nom du point
                         var nomPointFinal = "";
                         for (var m=nomPoint.length ; m >=0 ; m-- ){
                         nomPointFinal = nomPointFinal + nomPoint.charAt(m);
                         }
                         
                         if(latitudeGoalActuelle != latitude || longitudeGoalActuelle != longitude)
                         {
                         envoyerMessage("Vous avez un nouveau goal !");
                         alert("Vous avez un nouveau goal !")
                         }
                         latitudeGoalActuelle = latitude;
                         longitudeGoalActuelle = longitude;
                         
                         /*************** Creation du marker *****************/
                         var pinColor = "00CC00";
                         var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
                                                                    new google.maps.Size(21, 34),
                                                                    new google.maps.Point(0,0),
                                                                    new google.maps.Point(10, 34));
                         
                         var marker3 = new google.maps.Marker({
                                                              position: new google.maps.LatLng(longitude,latitude),
                                                              icon: pinImage,
                                                              title : nomPointFinal
                                                              });
                         
                         
                         var infowindow = new google.maps.InfoWindow({
                                                                     content: "Point à aller : " + nomPointFinal
                                                                     });
                         
                         
                         google.maps.event.addListener(marker3, 'click', function() {
                                                       infowindow.open(map, marker3);
                                                       });
                         
                         marker3.setMap(map);
                         google.maps.event.trigger(map, 'resize');
                         
                         
                         }},
                         
                         error: function( xhr, status, errorThrown ) {
                         alert( "Oups, Erreur !" );
                         console.log( "Error: " + errorThrown );
                         console.log( "Status: " + status );
                         console.dir( xhr );
                         },
                         complete: function( xhr, status ) {
                         }
                         });
                  }
                  
                  setTimeout(nextGoal,1000);
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  });
