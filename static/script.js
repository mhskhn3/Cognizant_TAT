function fetchSummary() {
    const supplier = $('#supplier').val();
    const product = $('#product').val();
    const country = $('#country').val();
    const region = $('#region').val();
  
    $.get('/api/summary', { supplier, product, country, region }, function(data) {
      $('#result').html(`
        <h3>Summary:</h3>
        <p><b>Open Work Orders:</b> ${data.open_work_orders}</p>
        <p><b>Pending xWS Activation:</b> ${data.pending_xws}</p>
        <p><b>Pending IDV:</b> ${data.pending_idv}</p>
        <p><b>Pending System Activation:</b> ${data.pending_system}</p>
        <hr>
        <p><b>Predicted xWS Time:</b> ${data.prediction_xws} days</p>
        <p><b>xWS → IDV Time:</b> ${data.prediction_xws_to_idv} days</p>
        <p><b>IDV → System Time:</b> ${data.prediction_idv_to_sys} days</p>
        <p><b>Running TAT:</b> ${data.avg_running_tat} days</p>
        <p><b><u>Total Estimated TAT:</u></b> ${data.total_estimated} days</p>
        <p><i>${data.remarks}</i></p>
      `);
    });
  }
  