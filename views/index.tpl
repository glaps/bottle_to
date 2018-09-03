<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Feedback</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-xs-4"></div>
                <h1 style="color:dodgerblue ;">Feedback</h1>
            </div> 
        </div>
    </div>
    <div class="container">
            <h3>example</h3>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-md-2"></div>
            <div class="col-md-8">
                <form class="form-group" method="post"  action="/">
                        <div class="form-group">
                            <label for="date1">ДАТА З:</label>
                            <input name="date1" type="date" class="form-control" id="date1" placeholder="2018-06-18">
                        </div>
                        <div class="form-group">
                            <label for="date2">ДАТА ПО:</label>
                            <input name="date2" type="date" class="form-control" id="date2" placeholder="2018-07-23">
                        </div>
                        <input type="submit" class="btn btn-primary" value="ОТРИМАТЬ">
                </form>
            </div>
            <div class="col-md-2"></div>
         </div>       
    </div>
    % if result:
    <div class="container">
        <table class="table table-dark">
            <thead>
                <tr>
                    <th scope="col">З</th>
                    <th scope="col">ПО</th>
                    <th scope="col">ЛИСТИ</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{a}}</td>
                    <td>{{b}}</td>
                    <td>{{result}}</td>
                </tr>
            </tbody>
        </table>
    </div>
    %end
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
</body>
</html>