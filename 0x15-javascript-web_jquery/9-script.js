fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    } else {
      return response.json();
    }
  })
  .then((data) => {
    $('#hello').text(data.hello);
  });
