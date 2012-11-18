
$(document).ready(function() {
  var winHeight = $(window).height() - 65;
  var date = new Date();
  var d = date.getDate();
  var m = date.getMonth();
  var y = date.getFullYear();
  
  var which_map = typeof trip_id === 'undefined' ? user_id : trip_id;
  
  var calendar = $('#calendar').fullCalendar({
    header: {
      left: '',
      center: '',
      right: ''
    },
    allDaySlot: false,
    defaultView: 'agendaDay',
    firstHour: 0,
    selectable: true,
    selectHelper: true,
    titleFormat: {
      day: 'dddd MM/dd'
    },
    eventClick: function(){
      editEvent();
    },
    select: function(start, end, allDay) {
      var title = prompt('Event Title:');
      if (title) {
        calendar.fullCalendar('renderEvent',
          {
            title: title,
            start: start,
            end: end,
            allDay: allDay
          },
          true // make the event "stick"
        );
      }
      calendar.fullCalendar('unselect');
    },
    editable: true,  
    height: winHeight,
    columnFormat: "'Events'",
    startParam: 'start__gte',
    endParam: 'end__lte',
    events: {
        url: '/api/v1/event/?trip=' + which_map + '&format=json',
        type: 'GET',
        error: function() {
            alert('Error Fetching Data');
        },
        success: function() {
            alert("done");
        }
    }
  });
  updateTitle();

  function updateTitle(){
    var view = $('#calendar').fullCalendar('getView');
    var lines = view.title.split(' ');
    $('.date').html(lines[0]);
    $('.sub-date').html(lines[1]);
  }

  function addEvent(){
    $('#new-edit').empty().append('New Event');
    $('#new-event-container').fadeToggle();
  }

  function editEvent(){
    $('#new-edit').empty().append('Edit Event');
    $('#new-event-container').fadeToggle();    
  }

  $('#title-prev').on('click', function(){
    $('#calendar').fullCalendar('prev');
    updateTitle();
  });
  $('#title-next').on('click', function(){
    $('#calendar').fullCalendar('next');
    updateTitle();
  });
  $('#title-new').on('click', function(){
    addEvent();
  });

  $('#cancel-add-edit').on('click', function(){
    $('#new-event-container').fadeToggle();    
  });

});
