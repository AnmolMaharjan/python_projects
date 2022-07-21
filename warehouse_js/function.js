
let token = {
    base_url: "http://172.16.10.10:8000/api"
}

const GetAvailability = (access_token) => 
{
    url = token.base_url + "/auth/availability/get-availability"
    fetch(url, 
    {
        method: "GET",
        headers: 
        {
            "Authorization": "Bearer "+ access_token,
            "Content-type": "application/json; charset=UTF-8",
        }
    }).then((res) => 
    {
        return res.json();
    }).then(function(_data_)
    {
        data=_data_['data'];
        document.getElementById('get_availability').innerHTML="Get Availability"
        let table = document.createElement('table');
        let header = document.createElement('tr');
        header.innerHTML = 
        `
            <th>ID</th>
            <th>User_ID</th>
            <th>Comments</th>
            <th>User_Available_date</th>
        `
        table.appendChild(header)
        data.forEach(element => {
            let row = document.createElement('tr');
            content=
            `
                <td>${element.id}</td>
                <td>${element.user_id}</td>
                <td>${element.comments}</td>
                <td>${element.user_available_date.available_date}</td>
            `
            row.innerHTML = content
            table.appendChild(row)
        });
        document.getElementById('get_availability_table').appendChild(table)
    }).catch(error => console.error('Error:', error))
}

const CreateAvailability = (access_token) =>
{
    // console.log(access_token);
    url = token.base_url+"/auth/availability/create-availability"
}

const ListJob = (access_token) =>
{
    console.log(access_token);
    url = token.base_url+"/auth/roles"
    fetch(url, 
    {
        method: "GET",
        headers:
        {
            "Authorization": "Bearer "+ access_token,
            "Content-type": "application/json; charset=UTF-8",
        }
    }).then((res) => 
    {
        return res.json();
    }).then(function(_data_)
    {
        console.log(_data_);
        data = _data_['result']
        console.log(data);
        document.getElementById('list_job').innerHTML="List Job"
        let table = document.createElement('table');
        let header = document.createElement('tr');
        header.innerHTML = 
        `
            <th>ID</th>
            <th>Name</th>
            <th>Guard Name</th>
            <th>Created At</th>
            <th>Updated At</th>
            <th colspan="3">Permissions</th>
        `
        table.appendChild(header)
        data.forEach(element => {
            let row = document.createElement('tr');
            content=
            `
                <td>${element.id}</td>
                <td>${element.name}</td>
                <td>${element.guard_name}</td>
                <td>${element.created_at}</td>
                <td>${element.updated_at}</td>
                <th>Person 1</th>
                <th>Person 2</th>
                <th>Person 3</th>
              
            `
            row.innerHTML = content
            table.appendChild(row)
        });
        document.getElementById('list_job_table').appendChild(table)
    }).catch(error => console.error('Error:', error))
}

const Login = () => {
    url = token.base_url + "/auth/login";
    fetch(url, {
        method: "POST",
        body: JSON.stringify({
            email: "admin@admin.com",
            password: "password",
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
        }
    }).then(function(response){      
         // Converting to JSON
        return response.json();
    }).then(function(data){
        let access_token = data["result"]["token"];
        return access_token;
    }).then(function(access_token){
        let a_token = access_token.split(".");
        var head = JSON.parse(atob(a_token[1]));
        var today = new Date();
        time = today.getDate();
        if (head.exp>time){
            GetAvailability(access_token);
            CreateAvailability(access_token);
            ListJob(access_token);
        }
    })
    .catch(error => console.error("Error:", error));
}
let access = Login()

