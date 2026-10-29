// SPDX-License-Identifier: {{licence}}
// The client of the {{name}} API, typed from api/openapi.json (`pnpm api` writes api-types.ts).
import createClient from "openapi-fetch";
import type { paths } from "./api-types";

export const api = createClient<paths>({ baseUrl: "/" });
