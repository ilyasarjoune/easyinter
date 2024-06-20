<!DOCTYPE html>
<html>
<head>
    <title>Internship Listings</title>
</head>
<body>
    <h1>Internship Listings</h1>
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Company</th>
                <th>Location</th>
                <th>Date</th>
                <th>Link</th>
            </tr>
        </thead>
        <tbody>
            @csrf
            @foreach($internships as $internship)
                <tr>
                    <td>{{ $internship->title }}</td>
                    <td>{{ $internship->company }}</td>
                    <td>{{ $internship->location }}</td>
                    <td>{{ $internship->date }}</td>
                    <td><a href="{{ $internship->link }}">Apply</a></td>
                </tr>
            @endforeach
        </tbody>
    </table>
</body>
</html>
