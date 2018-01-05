var data = [
{
parentEvent: 'ascension',
events:['momentum', 'la-trajectoire', 'daeroglisseur', 'drone-tech'],
max:[4,4,4,4],
as:[1,1,1,1]
},
{
parentEvent: 'modex',
events:['modex'],
max:[4],
as:[1]
},
{
parentEvent: 'pahal',
events:['greenx', 'vikalp', 'saksham', 'sampann', 'aagaz'],
max:[4,4,4,4,4],
as:[1,1,1,1,1]
},
{
parentEvent: 'supernova',
events:['scientists-utopia', 'astrophotography', 'astroquiz', 'exploring-interstellar'],
max:[3,1,1,2],
as:[1,1,1,1]
},
{
parentEvent: 'creatrix',
events:['minimize', 'iso', 'collage', 'avant-garde', 'animaze', '2d'],
max:[4,4,4,4,4,1],
as:[1,1,1,1,1,1]
},
{
parentEvent: 'riqueza',
events:['analiticity', 'bulls-floor', 'krackat', 'manthan','economists-enigma'],
max:[2,0,0,4,4],
as:[1,1,1,1,1]
},
{
parentEvent: 'byte-the-bits',
events:['international-coding-marathon', 'appathon', 'capture-the-flag'],
max:[0,3,0],
as:[0,0,1]
},
{
parentEvent: 'extreme-engineering',
events:['bridgeit', 'goldbergs-alley', 'axelerate', 'hydracs'],
max:[4,4,4,4],
as:[1,1,1,1]
},
{
parentEvent: 'robonex',
events:['robowars', 'pixelate', 'hurdlemania', 'mazeXplorer'],
max:[5,4,4,4],
as:[1,1,1,1]
}
/*{
parentEvent: 'game-dungeon',
events: ['nfs' , 'cs-go' , 'fifa'],
max:[0,4,0],
as:[1,1,1]
},
{
  parentEvent: 'dih-design-contest',
  events: ['classroom-furniture','classroom-cooling','classroom-sound-absorber','hostel-room-furniture' ,'mess-furniture'],
  max:[1,1,1,1,1],
  as:[1,1,1,1]
}*/
];

var workdata=[

{
  workshop: 'cryptocurrency',
  
},
{
  workshop: 'internet-of-things',
  
},
{
  workshop: 'autonomous-robotics-ardubotics',
  
},
{
  workshop: 'industrial-automation-plc-scada',
  
},
{
  workshop: 'automobile-mechanics-ic-engines',
  
},
{
  workshop: 'ethical-hacking-information-security',
  
},
{
  workshop: 'android-application-development',
  
},
{
  workshop: 'sixthsense-robotics',
  
},
{
  workshop: 'artificial-intelligence-machine-learning',
  
},
{
  workshop: 'augmented-reality',
  
},
{
  workshop: 'digital-marketing',
},
{
  workshop: 'e-commerce',
},
{
  workshop: 'bridge-design',
  
},
];
function findWithAttr(array, attr, value) {
  
    for(var i = 0; i < array.length; i += 1) {
        if(array[i][attr] === value) {
            return i;
        }
    }
    return -1;
}

  // create the module and name it app
	var app = angular.module('app', ['ngRoute']);

app.filter('propernames', function() {
    return function(x){
        var n="";       
        t=x;
        for(i=0;i<t.length;i++){
          if(i==0){
            n += t[i].toUpperCase();
            i++;
          }

          if(t[i]=='-'){
            n += ' ';
            i++;
            n += t[i].toUpperCase();
          }
          else{
            n+=t[i];
          }
        }
        return n;
    };
  });


	// configure our routes
	app.config(function($routeProvider) {
		$routeProvider

			// route for the home page
			.when('/profile', {
				templateUrl : '/static/pages/home.html',
				controller  : 'mainController'
			})
      .when("/",{
                  templateUrl:'/static/pages/home.html',
                  controller:'mainController',
              })
			// route for the about page
			.when('/eventreg', {
				templateUrl : '/static/pages/about.html',
				controller  : 'evnt-control'
			})
			.when('/eventreg/:param1/:param2', {
				templateUrl : '/static/pages/about.html',
				controller  : 'evnt-control'
			})

			.when('/workshop', {
				templateUrl : '/static/pages/form.html',
				controller  : 'workshop-cont'
			})

      .when('/startupreg/',{
                   templateUrl:'/static/pages/startupfair.html',
                   controller:'startup-cont'
      })

			.when('/changepassword', {
				templateUrl : '/static/pages/editprofile.html',
				controller  : 'memController'
			})

			.when('/editprofile', {
				templateUrl : '/static/pages/modify.html',
				controller  : 'mainController'
			})

			.when('/contacts', {
				templateUrl : '/static/pages/contacts.html',
				controller  : 'numController'
			})

			.when('/payment', {
				templateUrl : '/static/pages/payment.html',
				controller  : 'payController'
			})

			// route for the contact page
			.when('/contact', {
				templateUrl : '/static/pages/contact.html',
				controller  : 'contactController'
			})

      .otherwise({
                redirectTo: "/"
            });
	});

app.controller('evnt-control', ['$scope', '$window', '$http' ,'$routeParams', function($scope, $window,$http,$routeParams) {
   console.log("hi");
   var param1 = $routeParams.param1;
   var param2 = $routeParams.param2;

   console.log(param1+'  '+param2);
  $scope.parentEvent = '';

  $scope.max=0;
  $scope.a = [];
  $scope.options = $window.data;
  $scope.parentEventIndex = function(){
    return findWithAttr($scope.options,'events',$scope.parentEvent);
  };
  if (param1){
    $scope.parentEvent = $.grep($scope.options,function(n,i){ return n.parentEvent == param1})[0].events;
    $scope.selectedevent = param2;
    $scope.max = $scope.options[$scope.parentEventIndex()].max[$scope.parentEvent.indexOf($scope.selectedevent)];
  }
  $scope.counter = 0;
  $scope.members = [];
  $scope.user;
  $scope.leader = document.getElementById('userEmail').value;
  $scope.addMember = function(){
    if($scope.counter < $scope.max)
    $scope.members.push($scope.counter++);
  console.log($scope.a);
    };
  $scope.removeMember = function(z){
    console.log(z);
    $scope.members.splice(z,1);
    $scope.a.splice(z,1);
    $scope.counter--;
  };
   
   $scope.removeerror = function(z){
     var x=document.getElementsByClassName("abcd");
     var y=document.getElementsByClassName("parsley-errors-list");
     $(x[z]).removeClass("parsley-error");
     $(x[z]).removeClass("input-error");
     $(y[z+1]).hide();
   };
  $scope.update = function(){

    try{ 
    $scope.max = $scope.options[$scope.parentEventIndex()].max[$scope.parentEvent.indexOf($scope.selectedevent)];
    $scope.a  = new Array($scope.max);
        while($scope.members.length!=0)
    {
        $scope.members.pop();    
    }
    $scope.members=[];
    $scope.counter=0;
    return false;
  }
  catch(err){
    $scope.max = 0;$scope.counter = 0;
    return false;
  }
  };
  $scope.submitForm = function(event)
  {
     $(".team-reg-submit").html("Submitting!")
     var c = new Array();
     var i;
     for(i=0;i<$scope.counter;i++)
     {
       c.push($scope.a[i]);
     }
     data = {
      "eventSlug":$scope.selectedevent,
      "teamName":$scope.teamName,
      "members":c,
      "teamLeaderEmail":$scope.leader
     }
   console.log(data);
     
    $http({
      method: 'POST',
      url : '/events/register/',
      data : data
    })
    .success(function(data){
        console.log(data);
        if(data.status==1)
        {
           $scope.parentEvent='robonex';
          $scope.parentEvent='-- Select Parent Event --';
          $(".team-reg-submit").html("Submit");
         
          $("#error-message-display").html("Team successfully Registered");
          $("#error-message").show();
          location.reload(true);
          window.location.assign("#profile");
        }
        if(data.status==0)
        {

          $("#error-message-display").html(data.error);
          $("#error-message").show();
          $(".team-reg-submit").html("Submit");
        }
    })
  };


  }]);






	app.controller('mainController', function($scope,profileData,$http) {
		// create a message to display in our view
		$scope.editIndex = -1;
        $scope.editObject =   {
            name: "",
                technexId: "",
                college: "",
                year: "0",
                city: "",
                email: "",
                mobile: ""
        };
        $scope.showteams = true;
        $scope.showDetails = false;
        $scope.showWorkshops = true;
        $scope.teamArray = profileData.getTeamData();
        $scope.workshopArray = profileData.getWorkshopData();
        console.log($scope.workshopArray);
        console.log("skjdjfi");
        console.log($scope.teamArray.length);
        $scope.employeeArray = profileData.getStaffArray();
        $scope.profileEmail = document.getElementById('userEmail').value;



    $scope.position = function(data){
          var x=parseInt(data);
          switch(x)
          {
            case 0:
            return "--Select Your Year--";
            case 1:
            return "Freshmen";
            case 2:
            return "Sophomore";
            case 3:
            return "Junior";
            case 4:
            return "Senior";
            case 5:
            return "Senior";
            default:
            return "Student";
          }
        };

    $scope.deleteTeam = function(index){

          $http(
          {
          method: 'POST',
          url : '/events/teamDelete/',
          data : {"identifier":$scope.teamArray[index].teamId}
          }
          )
          .success(function(data){
            console.log(data);
            if(data.status==1)
            {
              $scope.teamArray.splice(index,1);
            }
            if(data.status==0)
            {
             console.log('Could not be Deleted!!!');
            }
          }
          );
        };

        $scope.editingPerson = function(personIndex){
            $scope.editObject = angular.copy($scope.employeeArray[personIndex]);
            $scope.editIndex = personIndex;
            console.log($scope.editObject);
            console.log($scope.employeeArray[personIndex]);
        };
        $scope.rmcls = function(){
          $("input").removeClass("input-error");
          $(".parsley-errors-list").hide();
          $("errormsg").hide();

        };



        //cancelEdit
        $scope.cancelEdit = function(){
            $scope.editIndex = -1;
            $scope.editObject = angular.copy();
        };

        $scope.saveEdit = function(personIndex){
          console.log(personIndex);
          var cdata = JSON.stringify($scope.editObject);
          console.log(cdata);
          var y=true;
             if(y)
             {
              if($("#forname").val()=="")
              {
                $("#forname").addClass("input-error");
                y=false;
              }
                if($("#forcollege").val()=="")
                {
                   $("#forcollege").addClass("input-error");
                y=false;
                }
                if($("#forcollegeyear").val()=="" || (isNaN(parseInt($("#forcollegeyear").val()))))
                {
                  $("#forcollegeyear").addClass("input-error");
                  y=false;  
                }
                if(!(isNaN(parseInt($("#forcollegeyear").val()))))
                {
                   var x=parseInt($("#forcollegeyear").val());
                  if(x>5 || x<1)
                  {
                    $("#forcollegeyear").addClass("input-error");
                    $("#collegeyearerr").show();
                    y=false;
                  }
                }
                if($("#forcity").val()=="")
                {
                  $("#forcity").addClass("input-error");
                  y=false;
                }
                if($("#formobile").val()=="")
                {
                  $("#formobile").addClass("input-error");
                  y=false;
                }
                if($("#formobile").val()!="")
                {
                  num=$("#formobile").val();
                  if((num.length!==10) || (isNaN(parseInt(num))) || (parseInt(num).toString().length  != num.length))
                   {
                       
                       $("#formobile").addClass("input-error");
                       $("#mobileerr").show();
                       y=false;
                   }

                }
             }
              
           if(y)
           {   
              $http({
      method: 'POST',
      url : '/updateProfile/',
      data : cdata
    })
    .success(function(data){
        console.log(data);
        if(data.status==1)
        {
            profileData.updateInfo(personIndex, $scope.editObject);
            $scope.editIndex = -1; 
            console.log($scope.editObject.name);
            //makeimg($scope.editObject.name);
            $("#user_name").html($scope.editObject.name);
           
           // window.location.assign("#profile"); 
            $scope.editObject = angular.copy();
            location.reload(true);
        }
        if(data.status==0)
        {
           console.log('Could not save Data!!!');
        }
    });
            
         }   
        };
	
  });
 

  app.controller("memController",function($scope,$http){

  $scope.oldpass="";
  $scope.newpass="";
  $scope.cnewpass="";
  
   $scope.cancel = function(){
     $scope.oldpass = null;
     $scope.newpass = null;
     $scope.cnewpass = null;
   }
   $scope.submit = function(){
    var y=true;
    if($scope.oldpass=="")
    {
      $("#old-pass").addClass("input-error"); 
      y=false; 
    }
    if(y)
    {
      if($scope.newpass=="")
      {
        $("#new-pass").addClass("input-error");
        y=false;
      }
     }
     if(y)
     {
      if($scope.cpass=="")
      {
        $("#confirm-new-pass").addClass("input-error");
        y=false;
      }
     }
     if(y)
     {
      if($scope.cnewpass!=$scope.newpass)
      {
        $("#confirm-new-pass").addClass("parsley-error");
        $("#pass-match-error").show();
        y=false;
      }
     }
     if(y)
     {
       data={
        "oldPass":$scope.oldpass,
       "newPass":$scope.newpass
     };
       $http({
        method: 'POST',
        url: '/resetpassword/',
        data: data
       }).success(function(data){
        if(data.status==1)
        {
           location.reload(true);
           window.location.assign("#profile");
        }
        if(data.status==0)
          {

            $("#resetpasserr").html(data.error);
            $("#resetpasserrmsg").show();
          }
       });

     }

    }
});

app.controller('workshop-cont', ['$scope', '$window', '$http','$routeParams' , function($scope, $window,$http,$routeParams) {
   var param1 = $routeParams.param1;
   //var param2 = $routeParams.param2;
  $scope.max=0;
  $scope.a =[];
  $scope.options = $window.workdata;
  $scope.workshop='';
  $scope.teamName="";
  $scope.counter = 0;
  $scope.members = [];
  if (param1){
    $scope.workshopObject = $.grep($scope.options,function(n,i){ return n.workshop == param1})[0];
    $scope.workshop = param1;
    $scope.max = $scope.workshopObject.max;
  }
  $scope.leader = document.getElementById('userEmail').value;
    $scope.membervalid= function(data)
   {
     var id=data.trim();
    var tid=id.length==7 && id.substring(0,2)=="TX" && !isNaN(parseInt(id.substring(2)));
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
       console.log("////");
       // console.log(tid);
      var email=re.test(id)
       return (email || tid);  
   }
    $scope.workshopIndex = function(){
      console.log($scope.options);
      console.log($scope.workshop);
      // console.log($scope.options);
    return findWithAttr($scope.options,'workshop',$scope.workshop);
  };
  $scope.addMember = function(){
    if($scope.counter < $scope.max)
    $scope.members.push($scope.counter++);
  console.log($scope.a);
    };
  $scope.removeMember = function(z){
    console.log(z);
    $scope.members.splice(z,1);
    $scope.a.splice(z,1);
    $scope.counter--;
  };
  

    $scope.update = function(){
      console.log($scope.max);

    try{ 
    $scope.max = $scope.options[$scope.workshopIndex()].max;
    console.log($scope.workshopIndex());
    $scope.a  = [];
        while($scope.members.length!=0)
    {
        $scope.members.pop();    
    }
    $scope.members=[];
    $scope.counter=0;
    return false;
  }
  catch(err){
    $scope.max = 0;$scope.counter = 0;
    return false;
  }
  };
  $scope.removeerror = function(z){
     var x=document.getElementsByClassName("abcd");
     var y=document.getElementsByClassName("parsley-errors-list");
     $(x[z]).removeClass("parsley-error");
     $(x[z]).removeClass("input-error");
     $(y[z+1]).hide();
   };
  $scope.submitForm = function(event)
  {
    // console.log($scope.a);
    console.log($scope.teamName);
    var x=true;
    if(x)
    {
       // console.log($scope.workshop);
      if($scope.workshop =="" || $scope.workshop==null)
        {x=false;
          $("#parentevent").addClass("input-error");
        }
    }
    /*if(x)
    {
       if($scope.max!=1)
       {
        if($scope.teamName=="")
        {
           x=false;
          $("#teamName").addClass("input-error");
           }
       }

    }*/
     if(x)
     {
      if($scope.leader=="")
      {
        $("#team-leader").addClass("input-error");
        x=false;
      }
     }
     if(x)
     {
      if(!$scope.membervalid($("#team-leader").val()))
      {
        $("#team-leader").addClass("parsley-error");
        $("#team-leader-invalid").show();
        x=false;
      }
     }
     var z=$(".abcd");
     var z1=$(".parsley-errors-list");
     if(x)
     {
       var i;
       
       for(i=0;i<z.length;i++)
       {
          if($(z[i]).val()=="")
          {
            $(z[i]).addClass("input-error");
            x=false;
          }

       }
     }
     if(x)
     {
       var i;
       for(i=0;i<z.length;i++)
       {
        if(!$scope.membervalid($(z[i]).val()))
        {
          $(z[i]).addClass("parsley-error");
          $(z1[i+1]).show();
          x=false;
        }
       }
     }
     if(x)
     {
      $(".team-reg-submit").html("Submitting!")
       console.log($scope.a);
       data={
        'workshopSlug':$scope.workshop,
        'teamName': $scope.leader,
        'teamLeaderEmail': $scope.leader,
        'members':$scope.a
       }
        $http({
              method:'POST',
              url:'/workshopRegister/',
              data: data
             }).success(function(data){
              $(".team-reg-submit").html("Submit");
              console.log(data);
                if(data.status==0)
                {
                   $("#error-message-display").html(data.error);
                   $("#error-message").show();
                   $(".team-reg-submit").html("Submit");
                }
                if(data.status==1)
                {
                   
                   window.location.assign("#profile");
                   location.reload(true);
                }
             });
     }

  }

}]);

app.controller('startup-cont', ['$scope', '$window', '$http' , function($scope, $window,$http) {
  
  $scope.visible1 = false;
  $scope.visible2 = false;
  $scope.a = [];
  $scope.options = $window.data;
  $scope.counter = 0;
  $scope.members = [];
  $scope.user;
  $scope.ideas="";
  $scope.teamName="";
  $scope.link="";
  $scope.funding="";
  $scope.startuptype="";
  $scope.description="";
  $scope.year="Founding Year";
  $scope.indlist = [];
  $scope.bslist = [];
  $scope.leader = document.getElementById('userEmail').value;

  $scope.showhide1 = function () {
    //If DIV is visible it will be hidden and vice versa.
    $scope.visible1 = true;
    $scope.visible2 = false;
    $scope.startuptype="Ventura";
  }
  $scope.showhide2 = function () {
    //If DIV is visible it will be hidden and vice versa.
    $scope.visible1 = false;
    $scope.visible2 = true;
    $scope.startuptype="Startupbattle";
  }

  $scope.parentEventIndex = function(){
    return findWithAttr($scope.options,'events',$scope.parentEvent);
  };
  $scope.addMember = function(){
    $scope.members.push($scope.counter++);
    };
  $scope.removeMember = function(z){
    $scope.members.splice(z,1);
    $scope.a.splice(z,1);
    $scope.counter--;
  };
   
   $scope.removeerror = function(z){
     var x=document.getElementsByClassName("abcd");
     var y=document.getElementsByClassName("parsley-errors-list");
     $(x[z]).removeClass("parsley-error");
     $(x[z]).removeClass("input-error");
     $(y[z+1]).hide();
   };
  $scope.update = function(){

    try{ 
    $scope.max = $scope.options[$scope.parentEventIndex()].max[$scope.parentEvent.indexOf($scope.selectedevent)];
    $scope.a  = new Array($scope.max);
        while($scope.members.length!=0)
    {
        $scope.members.pop();    
    }
    $scope.members=[];
    $scope.counter=0;
    return false;
  }
  catch(err){
    $scope.max = 0;$scope.counter = 0;
    return false;
  }
  };
   $scope.membervalid= function(data)
   {
     var id=data.trim();
    var tid=id.length==7 && id.substring(0,2)=="TX" && !isNaN(parseInt(id.substring(2)));
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
       console.log("////");
       console.log(tid);
      var email=re.test(id)
       return (email || tid);  
   }
  $scope.submitForm = function(event)
  {

     var x=true;
     console.log($scope.teamName);
     if($scope.teamName=="")
     {
      $("#teamName").addClass("input-error");
      x=false;
      console.log("empty");
     }
     /*if(x)
     {
       if($scope.interests=="")
       {
        $("#interests").addClass("input-error");
        x=false;
       }
     }*/
     if(x)
     {
      if($scope.description=="")
      {
        $("#description").addClass("input-error");
        x=false;
      }
     }
     if(x)
     {
      if($scope.year=="Founding Year"&&$scope.visible2)
        {
          $("#year").addClass("input-error");
          x=false;
        }
      else if($scope.visible1){
        $scope.year=0;
      }
     }
     if(x&&$scope.visible2)
      {
        if($scope.funding=="")
        {
          $("#error-message").show();
          $("#error-message-display").html("You have not selected if you have received funding!!")
          x=false;
        }
      }
     /*if(x)
      {
        var z=$(".industrylist input");
        for(var i=0;i<24;i++)
        {
          if($(z[i]).prop("checked")==true)
          { 
            console.log($(z[i]).value);
            $scope.indlist.push($(z[i]).val());
             
        }
      }*/
        /*if($scope.indlist.length==0)
        {
            $("#error-message-display").html("Please, Select atleast 1 primary industry");
            $("#error-message").show();
            x=false;
        }*/
        /*if($scope.indlist.length>3)
        {
          $("#error-message-display").html("Please, Select atmost 3 primary industry");
            $("#error-message").show();
            x=false;
            console.log($scope.indlist);
            $scope.indlist=[];
        }*/
        
      
      if(x&&$scope.visible1)
      {
        var z=$(".businesslist1 input");
        for(var i=0;i<4;i++)
        {
          if($(z[i]).prop("checked")==true)
          {
            $scope.bslist.push($(z[i]).val());
          }
        }
        if($scope.bslist.length==0)
        {
          $("#error-message-display").html("Please, Select atleast 1 Startup type");
            $("#error-message").show();
            x=false;
        }
      }
      if(x&&$scope.visible2)
      {
        var z=$(".businesslist2 input");
        for(var i=0;i<4;i++)
        {
          if($(z[i]).prop("checked")==true)
          {
            $scope.bslist.push($(z[i]).val());
          }  
        }
        if($scope.bslist.length==0)
        {
          $("#error-message-display").html("Please, Select atleast 1 Startup type");
            $("#error-message").show();
            x=false;
        }
      }
      


     if(x)
     {
      if($scope.leader=="")
      {
        $("#team-leader").addClass("input-error");
        x=false;
      }
     }
     if(x)
     {
      if(!$scope.membervalid($("#team-leader").val()))
      {
        $("#team-leader").addClass("parsley-error");
        $("#team-leader-invalid").show();
        x=false;
      }
     }
     var z=$(".abcd");
     var z1=$(".parsley-errors-list");
     if(x)
     {
       var i;
       
       for(i=0;i<z.length;i++)
       {
          if($(z[i]).val()=="")
          {
            $(z[i]).addClass("input-error");
            x=false;
          }

       }
     }
     if(x)
     {
       var i;
       for(i=0;i<z.length;i++)
       {
        if(!$scope.membervalid($(z[i]).val()))
        {
          $(z[i]).addClass("parsley-error");
          $(z1[i+1]).show();
          x=false;
        }
       }
     }
      
      if(x)
      {
             $(".team-reg-submit").html("Submitting!");
             data={
              "teamName":$scope.teamName,
              "memberMails":$scope.a,
              "teamLeader":$scope.leader,
              "startuptype":$scope.startuptype,
              "description":$scope.description,
              "year": $scope.year,
              //"pindustry": $scope.indlist,
              "btype": $scope.bslist,
              "link": $scope.link,
              "funding": $scope.funding
             }
             $scope.indlist=[];
             $scope.bslist=[];
             $http({
              method:'POST',
              url:'/startupregister/',
              data: data
             }).success(function(data){
              $(".team-reg-submit").html("Submit");
              console.log(data);
                if(data.status==0)
                {
                   $("#error-message-display").html(data.error);
                   $("#error-message").show();
                   
                }
                if(data.status==1)
                {
                   
                   window.location.assign("#profile");
                   location.reload(true);
                }
             });


      }
  };
 }]);
  