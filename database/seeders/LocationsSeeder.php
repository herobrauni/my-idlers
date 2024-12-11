<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class LocationsSeeder extends Seeder
{
    public function run()
    { //Note add any new locations at the bottom of the array
        $locations = [
            ['name' => 'My basement'],
        ];

        DB::table('locations')->insert($locations);
    }
}
