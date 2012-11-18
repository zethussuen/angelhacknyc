
$(document).ready(function() {
  var winHeight = $(window).height() - 65;
  var date = new Date();
  var d = date.getDate();
  var m = date.getMonth();
  var y = date.getFullYear();
  
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

  $('#title-prev').click(function(){
    $('#calendar').fullCalendar('prev');
    updateTitle();
  });
  $('#title-next').click(function(){
    $('#calendar').fullCalendar('next');
    updateTitle();
  });
  $('#title-new').click(function(){
    addEvent();
  });

  $('#cancel-add-edit').click(function(){
    $('#new-event-container').fadeToggle();    
  });

});
