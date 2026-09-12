# KH05 Repo Ownership Weights

Generated: 2026-05-12T09:14:35.227392Z

Source: local Git history from `/Users/oleksandrgrytsenko/Documents/OFS_REPOS`; OraHub MR metadata was not available locally, so this is commit-derived v1 with schema room for MR enrichment later.

Scoring: recent commits since 2023-05-12, exponentially decayed with 365-day half-life; file count and capped line churn add weight; all-time commits are retained as fallback evidence.

Use policy: prefer the top repo owner for normal tasks; for high-risk work, combine repo weight with role fit from `@kh05 team`.

## app_server
- Note: repo has 4 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Oleksiy Tymofiev | `oleksiy_tymofeyev` | 50.7% | 1206 | 2026-05-11T22:41:55Z | Senior C++ Developer |
| 2 | Sergiy Pisklow | `sergii_pisklov` | 19.7% | 473 | 2026-05-11T15:00:29Z | Senior C++ Developer |
| 3 | Aliaksandr Bulynka | `aliaksandr.bulynka` | 11.9% | 262 | 2026-05-06T21:10:44Z | Senior C++ Developer |
| 4 | Andrey Shapovalov | `andrey_shapovalov` | 11.5% | 280 | 2026-03-12T10:34:48Z | Senior Java Developer |
| 5 | Ivan Trufanov | `ivan_trufanov` | 3.3% | 115 | 2025-11-06T10:18:10Z | Senior Java Developer |

Top path hints:
- `src/app_server`: Oleksiy Tymofiev 55.0%, Sergiy Pisklow 30.1%, Aliaksandr Bulynka 8.6%
- `src/tests`: Oleksiy Tymofiev 60.7%, Alyona Kleba 16.8%, Sergiy Pisklow 11.2%
- `app_server/mod_app`: Oleksiy Tymofiev 59.4%, Sergiy Pisklow 29.8%, Aliaksandr Bulynka 10.8%
- `(root)`: Andrey Shapovalov 48.9%, Ivan Trufanov 25.3%, Aliaksandr Bulynka 16.6%
- `src/general`: Oleksiy Tymofiev 34.9%, Aliaksandr Bulynka 31.2%, Sergiy Pisklow 30.3%

## cmdb
- Note: repo has 4 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Volodymyr Mukhachov | `volodymyr_mukhachov` | 68.6% | 38 | 2026-03-24T18:27:38Z | Senior Database Developer |
| 2 | Andrey Shapovalov | `andrey_shapovalov` | 31.4% | 21 | 2026-03-11T17:04:36Z | Senior Java Developer |

Top path hints:
- `CMDB/migration`: Volodymyr Mukhachov 89.1%, Andrey Shapovalov 10.9%
- `helm/cmdb`: Andrey Shapovalov 69.4%, Volodymyr Mukhachov 30.6%
- `CMDB/src`: Volodymyr Mukhachov 98.4%, Andrey Shapovalov 1.6%
- `CMDB/test`: Volodymyr Mukhachov 99.4%, Andrey Shapovalov 0.6%
- `deployment/spinnaker`: Andrey Shapovalov 100.0%

## core-pod-parameters
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Ivan Trufanov | `ivan_trufanov` | 89.1% | 24 | 2025-05-07T11:02:45Z | Senior Java Developer |
| 2 | Andrey Shapovalov | `andrey_shapovalov` | 10.9% | 2 | 2026-02-27T18:55:26Z | Senior Java Developer |

Top path hints:
- `deploymentConfigs/field-service`: Ivan Trufanov 85.5%, Andrey Shapovalov 14.4%
- `(root)`: Ivan Trufanov 100.0%

## daily-extract
- Note: repo has 6 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Andrey Shapovalov | `andrey_shapovalov` | 36.4% | 68 | 2026-04-16T12:27:18Z | Senior Java Developer |
| 2 | Aliaksandr Bulynka | `aliaksandr.bulynka` | 28.3% | 46 | 2026-05-05T15:22:22Z | Senior C++ Developer |
| 3 | Ivan Trufanov | `ivan_trufanov` | 20.3% | 83 | 2026-03-25T15:43:44Z | Senior Java Developer |
| 4 | Sergiy Pisklow | `sergii_pisklov` | 14.1% | 57 | 2025-10-22T14:01:06Z | Senior C++ Developer |
| 5 | Volodymyr Mukhachov | `volodymyr_mukhachov` | 0.8% | 5 | 2025-04-21T11:48:51Z | Senior Database Developer |

Top path hints:
- `functional_tests/src`: Andrey Shapovalov 72.4%, Ivan Trufanov 12.0%, Sergiy Pisklow 10.5%
- `src/main`: Aliaksandr Bulynka 53.5%, Andrey Shapovalov 20.1%, Sergiy Pisklow 13.6%
- `helm/daily-extract`: Ivan Trufanov 43.4%, Sergiy Pisklow 23.5%, Aliaksandr Bulynka 17.0%
- `intg/helm`: Andrey Shapovalov 54.2%, Aliaksandr Bulynka 45.8%
- `src/test`: Aliaksandr Bulynka 61.6%, Sergiy Pisklow 15.6%, Andrey Shapovalov 12.7%

## daily-extract-scheduler
- Note: repo has 4 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Andrey Shapovalov | `andrey_shapovalov` | 42.8% | 65 | 2026-04-30T11:27:11Z | Senior Java Developer |
| 2 | Aliaksandr Bulynka | `aliaksandr.bulynka` | 33.4% | 48 | 2026-05-05T16:45:00Z | Senior C++ Developer |
| 3 | Ivan Trufanov | `ivan_trufanov` | 21.4% | 54 | 2026-03-31T10:22:55Z | Senior Java Developer |
| 4 | Sergiy Pisklow | `sergii_pisklov` | 2.3% | 11 | 2025-01-23T15:50:30Z | Senior C++ Developer |

Top path hints:
- `intg/helm`: Andrey Shapovalov 54.3%, Aliaksandr Bulynka 45.3%, Ivan Trufanov 0.4%
- `src/main`: Aliaksandr Bulynka 44.9%, Andrey Shapovalov 28.9%, Ivan Trufanov 19.9%
- `src/test`: Ivan Trufanov 35.8%, Aliaksandr Bulynka 31.0%, Andrey Shapovalov 29.0%
- `(root)`: Aliaksandr Bulynka 49.6%, Andrey Shapovalov 47.5%, Ivan Trufanov 2.9%
- `helm/daily-extract-scheduler`: Ivan Trufanov 74.6%, Andrey Shapovalov 18.2%, Sergiy Pisklow 4.1%

## database
- Note: repo has 5 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Oleksiy Bondarenko | `oleksiy.bondarenko` | 60.7% | 160 | 2026-05-07T14:47:17Z | Senior Fusion Database Developer |
| 2 | Volodymyr Mukhachov | `volodymyr_mukhachov` | 34.7% | 156 | 2026-04-16T11:46:32Z | Senior Database Developer |
| 3 | Andrey Shapovalov | `andrey_shapovalov` | 2.8% | 24 | 2025-04-02T08:57:14Z | Senior Java Developer |
| 4 | Alexander Yaroshchuk | `alexander_yaroshchuk` | 1.2% | 2 | 2026-04-16T11:46:32Z | Senior Database Developer |
| 5 | Oleksiy Tymofiev | `oleksiy_tymofeyev` | 0.4% | 6 | 2024-01-26T15:04:27Z | Senior C++ Developer |

Top path hints:
- `feature-dev/26.07.00.00`: Oleksiy Bondarenko 95.9%, Volodymyr Mukhachov 4.1%
- `feature-dev/26.04.00.00`: Oleksiy Bondarenko 82.6%, Volodymyr Mukhachov 17.4%
- `feature-dev/25.10.00.00`: Oleksiy Bondarenko 83.3%, Volodymyr Mukhachov 16.7%
- `feature-dev/24.04.00.00`: Volodymyr Mukhachov 97.1%, Sergiy Pisklow 1.4%, Oleksiy Tymofiev 1.4%
- `feature-dev/26.01.00.00`: Oleksiy Bondarenko 100.0%

## db-maintenance
- Note: repo has 4 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Andrey Shapovalov | `andrey_shapovalov` | 88.0% | 395 | 2026-04-23T13:36:53Z | Senior Java Developer |
| 2 | Volodymyr Mukhachov | `volodymyr_mukhachov` | 11.3% | 75 | 2026-05-11T15:45:11Z | Senior Database Developer |
| 3 | Sergiy Pisklow | `sergii_pisklov` | 0.5% | 3 | 2024-05-03T08:33:30Z | Senior C++ Developer |
| 4 | Oleksiy Tymofiev | `oleksiy_tymofeyev` | 0.3% | 6 | 2024-01-25T13:27:14Z | Senior C++ Developer |

Top path hints:
- `src/main`: Andrey Shapovalov 90.8%, Volodymyr Mukhachov 8.4%, Sergiy Pisklow 0.5%
- `src/test`: Andrey Shapovalov 81.8%, Volodymyr Mukhachov 16.9%, Sergiy Pisklow 1.1%
- `intg/helm`: Andrey Shapovalov 92.6%, Volodymyr Mukhachov 7.4%
- `(root)`: Andrey Shapovalov 99.7%, Volodymyr Mukhachov 0.3%, Sergiy Pisklow 0.0%
- `helm/db-maintenance`: Andrey Shapovalov 68.1%, Volodymyr Mukhachov 31.3%, Oleksiy Tymofiev 0.6%

## db-updater
- Note: repo has 1 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Andrey Shapovalov | `andrey_shapovalov` | 81.7% | 687 | 2026-05-12T04:15:06Z | Senior Java Developer |
| 2 | Oleksiy Bondarenko | `oleksiy.bondarenko` | 9.2% | 106 | 2025-12-31T15:09:13Z | Senior Fusion Database Developer |
| 3 | Volodymyr Mukhachov | `volodymyr_mukhachov` | 9.0% | 148 | 2026-05-11T14:41:30Z | Senior Database Developer |
| 4 | Sergiy Pisklow | `sergii_pisklov` | 0.1% | 2 | 2023-12-19T14:22:50Z | Senior C++ Developer |
| 5 | Oleksiy Tymofiev | `oleksiy_tymofeyev` | 0.1% | 2 | 2024-01-26T15:04:27Z | Senior C++ Developer |

Top path hints:
- `core/src`: Andrey Shapovalov 99.6%, Volodymyr Mukhachov 0.4%
- `application/src`: Andrey Shapovalov 100.0%, Sergiy Pisklow 0.0%, Volodymyr Mukhachov 0.0%
- `database/feature-dev`: Oleksiy Bondarenko 52.6%, Volodymyr Mukhachov 41.5%, Andrey Shapovalov 5.5%
- `functional_tests/src`: Andrey Shapovalov 95.5%, Volodymyr Mukhachov 4.5%
- `intg/helm`: Andrey Shapovalov 100.0%

## dev-config-provider
- Note: repo has 4 local dirty entries; fetched remote history was still used.
- No matched KH05 recent commits in scoring window.

## file-storage-agent
- Note: repo has 1 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Ivan Trufanov | `ivan_trufanov` | 85.5% | 166 | 2026-05-11T13:40:49Z | Senior Java Developer |
| 2 | Andrey Shapovalov | `andrey_shapovalov` | 14.5% | 25 | 2026-05-05T10:10:43Z | Senior Java Developer |

Top path hints:
- `microservice/src`: Ivan Trufanov 96.8%, Andrey Shapovalov 3.2%
- `intg/helm`: Ivan Trufanov 60.0%, Andrey Shapovalov 40.0%
- `(root)`: Ivan Trufanov 71.2%, Andrey Shapovalov 28.8%
- `functional_tests/src`: Ivan Trufanov 99.6%, Andrey Shapovalov 0.4%
- `devenv/rest`: Ivan Trufanov 91.8%, Andrey Shapovalov 8.2%

## platform-fe
- Note: repo has 7 local dirty entries; fetched remote history was still used.
- No matched KH05 recent commits in scoring window.

## platform-lcm
- Note: repo has 9 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Ivan Trufanov | `ivan_trufanov` | 89.9% | 757 | 2026-05-07T15:13:23Z | Senior Java Developer |
| 2 | Andrey Shapovalov | `andrey_shapovalov` | 9.8% | 118 | 2026-02-11T19:25:40Z | Senior Java Developer |
| 3 | Sergiy Pisklow | `sergii_pisklov` | 0.3% | 4 | 2025-04-16T14:24:04Z | Senior C++ Developer |

Top path hints:
- `microservice/src`: Ivan Trufanov 93.6%, Andrey Shapovalov 5.7%, Sergiy Pisklow 0.7%
- `helm/platform-lcm`: Ivan Trufanov 90.0%, Andrey Shapovalov 10.0%
- `(root)`: Ivan Trufanov 81.7%, Andrey Shapovalov 18.3%
- `intg/helm`: Ivan Trufanov 92.2%, Andrey Shapovalov 7.8%
- `helm-charts/platform-be`: Ivan Trufanov 98.9%, Andrey Shapovalov 1.1%

## platform-updates-launcher
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Andrey Shapovalov | `andrey_shapovalov` | 100.0% | 68 | 2025-10-31T14:59:10Z | Senior Java Developer |

Top path hints:
- `helm/platform-updates-launcher`: Andrey Shapovalov 100.0%
- `src/main`: Andrey Shapovalov 100.0%
- `functional_tests/src`: Andrey Shapovalov 100.0%
- `src/test`: Andrey Shapovalov 100.0%
- `functional_tests_images/pul-mock-vault`: Andrey Shapovalov 100.0%

## web
- Note: repo has 21 local dirty entries; fetched remote history was still used.
| Rank | Developer | orahub_id | Weight | Recent commits | Last commit | Role note |
| --- | --- | --- | ---: | ---: | --- | --- |
| 1 | Oleksiy Tymofiev | `oleksiy_tymofeyev` | 45.1% | 52 | 2025-10-30T19:41:37Z | Senior C++ Developer |
| 2 | Aliaksandr Bulynka | `aliaksandr.bulynka` | 32.2% | 14 | 2026-04-15T11:25:56Z | Senior C++ Developer |
| 3 | Alyona Kleba | `alyona_kleba` | 12.2% | 6 | 2026-01-27T00:56:42Z | QA Automation |
| 4 | Sergiy Pisklow | `sergii_pisklov` | 7.3% | 13 | 2024-11-25T10:35:06Z | Senior C++ Developer |
| 5 | Volodymyr Mukhachov | `volodymyr_mukhachov` | 3.1% | 2 | 2025-09-01T07:38:06Z | Senior Database Developer |

Top path hints:
- `wwwclasses/Api`: Alyona Kleba 55.4%, Aliaksandr Bulynka 18.1%, Sergiy Pisklow 15.6%
- `tests/unit`: Aliaksandr Bulynka 57.0%, Oleksiy Tymofiev 38.5%, Sergiy Pisklow 4.5%
- `wwwscripts/web`: Oleksiy Tymofiev 71.4%, Aliaksandr Bulynka 28.6%
- `wwwclasses/Manage`: Oleksiy Tymofiev 64.9%, Volodymyr Mukhachov 34.4%, Aliaksandr Bulynka 0.7%
- `wwwscripts/mobile`: Oleksiy Tymofiev 90.9%, Aliaksandr Bulynka 9.1%

## Developers With Little Or No Git Evidence

- Dmytro Lehenkyi (`dmytro_l_lehenkyi`): 0 recent matched commits, 0 all-time matched commits. Route by role/manual knowledge unless future MR/Jira data adds evidence.
