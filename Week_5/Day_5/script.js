const robots = [{
        id: 1,
        name: 'Leanne Graham',
        username: 'Bret',
        email: 'Sincere@april.biz',
        image: '1'
    },
    {
        id: 2,
        name: 'Ervin Howell',
        username: 'Antonette',
        email: 'Shanna@melissa.tv',
        image: '2'
    },
    {
        id: 3,
        name: 'Clementine Bauch',
        username: 'Samantha',
        email: 'Nathan@yesenia.net',
        image: '3'
    },
    {
        id: 4,
        name: 'Patricia Lebsack',
        username: 'Karianne',
        email: 'Julianne.OConner@kory.org',
        image: '4'
    },
    {
        id: 5,
        name: 'Chelsey Dietrich',
        username: 'Kamren',
        email: 'Lucio_Hettinger@annie.ca',
        image: '5'
    },
    {
        id: 6,
        name: 'Mrs. Dennis Schulist',
        username: 'Leopoldo_Corkery',
        email: 'Karley_Dach@jasper.info',
        image: '6'
    },
    {
        id: 7,
        name: 'Kurtis Weissnat',
        username: 'Elwyn.Skiles',
        email: 'Telly.Hoeger@billy.biz',
        image: '7'
    },
    {
        id: 8,
        name: 'Nicholas Runolfsdottir V',
        username: 'Maxime_Nienow',
        email: 'Sherwood@rosamond.me',
        image: '8'
    },
    {
        id: 9,
        name: 'Glenna Reichert',
        username: 'Delphine',
        email: 'Chaim_McDermott@dana.io',
        image: '9'
    },
    {
        id: 10,
        name: 'Clementina DuBuque',
        username: 'Moriah.Stanton',
        email: 'Rey.Padberg@karina.biz',
        image: '10'
    }
];

let formattedRobots = []

function loadRobots() {
    robots.forEach((robot) => {
        formattedRobots.push(`
            <div class="robot" id="robot-${robot.id}">
                <img class="robot-img" src="robo-images/${robot.image}.png">
                <h3>@${robot.username}</h3>
                <h2>${robot.name}</h2>
                <p>${robot.email}</p>
            </div>            
    `)
    })
    $('#robots').html(formattedRobots)
}

loadRobots()

$("#search").on("input", () => {
    query = $("#search").val().toLowerCase()
    console.log(query)
    filteredRobots = []

    robots.filter(robot => robot.name.toLowerCase().includes(query)).forEach((robot) => {
        filteredRobots.push(`
            <div class="robot" id="robot-${robot.id}">
            <img class="robot-img" src="robo-images/${robot.image}.png">
            <h3>@${robot.username}</h3>
            <h2>${robot.name}</h2>
            <p>${robot.email}</p>
            </div>            
    `)
    })
    $('#robots').html(filteredRobots)
})