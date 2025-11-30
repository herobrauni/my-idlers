<?php

namespace Tests\Feature;

use App\Models\Domains;
use App\Models\Pricing;
use App\Models\Providers;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class DomainsTest extends TestCase
{
    use RefreshDatabase;

    public function test_domains_index_contains_data_order_attribute()
    {
        $user = User::factory()->create();

        $provider = Providers::create(['name' => 'Test Provider']);

        $domain = Domains::create([
            'id' => 'testdom1',
            'domain' => 'test',
            'extension' => 'com',
            'provider_id' => $provider->id,
            'owned_since' => now(),
        ]);

        $nextDueDate = now()->addDays(30)->format('Y-m-d');

        Pricing::create([
            'service_id' => $domain->id,
            'service_type' => 4, // Assuming 4 is domain
            'currency' => 'USD',
            'price' => 10.00,
            'term' => 1,
            'as_usd' => 10.00,
            'usd_per_month' => 0.83,
            'next_due_date' => $nextDueDate,
        ]);

        $response = $this->actingAs($user)->get(route('domains.index'));

        $response->assertStatus(200);
        $response->assertSee('data-order="' . $nextDueDate . '"', false);
    }
}
