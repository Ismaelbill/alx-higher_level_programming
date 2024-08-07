const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (d) => {
  d.results.forEach(el => {
    $('UL#list_movies').append(`<li>${el.title}</li>`);
  });
});
