$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (d) => {
  $('DIV#character').text(d.name);
});
