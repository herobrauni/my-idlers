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
            ['name' => "Bakker IT"],
            ['name' => "HeartBeatIT"],
            ['name' => "Host-C"],
            ['name' => "HostDZire"],
            ['name' => "Kuroit"],
            ['name' => "Naranja"],
            ['name' => "ProHost24"],
            ['name' => "TNAhosting"],
            ['name' => "xTom"],
            ['name' => "Oracle"],
            ['name' => "Hetzner"],
            ['name' => "N100"],
            ['name' => "NAS"],
            ['name' => "Myself"],
        ];

        DB::table('providers')->insert($providers);
    }
}
