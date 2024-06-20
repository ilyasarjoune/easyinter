<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Internship;

class InternshipController extends Controller
{
    public function index()
{
    $internships = Internship::all();
    return view('index', compact('internships'));
    
}
    public function store(Request $request)
    {
        $internships = $request->all();
        
        foreach ($internships as $internship) {
            Internship::create([
                'title' => $internship['title'],
                'company' => $internship['company'],
                'location' => $internship['location'],
                'date' => $internship['date'],
                'link' => $internship['link'],
            ]);
        }
        
        return response()->json(['message' => 'Internships successfully stored'], 200);
    }
}
