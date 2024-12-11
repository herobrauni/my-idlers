<?php

namespace Database\Seeders;

use App\Models\Providers;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class ProvidersSeeder extends Seeder
{
    public function run()
    {

        $providers = [
            ['name' => "Myself"],
        ];

        DB::table('providers')->insert($providers);
    }
}
