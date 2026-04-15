# passwordless-authentication
An authentication API gateway that models Substack's approach, using 2FA to authenticate users instead of traditional password authentication.


## Features


## Endpoints
<style>
    .dark-table {
        background-color: #1a1a1a; 
        color: #e0e0e0;           
        border-collapse: collapse; 
        width: 100%;
    }

    .dark-table th, 
    .dark-table td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #333;
        border-left: 1px solid #333; 
        border-right: 1px solid #333;    
    }

    .dark-table th {
        background-color: #252525;
        color: #ffffff;
    }

    .dark-table {
        border: 1px solid #333;
    }
</style>

<table class="dark-table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Method</th>
            <th>Path</th>
            <th>Content-Type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Login</td>
            <td>POST</td>
            <td><code>/api/login/</code></td>
            <td><code>application/json</code></td>
        </tr>
    </tbody>
</table>