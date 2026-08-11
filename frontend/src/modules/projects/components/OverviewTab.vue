<template>

     <TabPanel value="0">
                     <div class="tw-flex tw-flex-col tw-gap-3">
                        <div
                           class="tw-mt-3 tw-flex tw-w-full tw-flex-wrap tw-justify-between tw-gap-4 lg:tw-gap-0">
                           <OverviewCard
                              mainText="Total Endpoints"
                              :subText="1"
                              gradientFrom="tw-from-pulse-cyan"
                              icon="pi pi-server"
                              iconColor="tw-text-pulse-cyan"
                              iconBg="tw-bg-pulse-cyan/20"
                              shadow="tw-shadow-[0_0_20px_rgba(34,211,238,0.3)]" />
                           <OverviewCard
                              mainText="Avg. Response Time"
                              :subText="1"
                              gradientFrom="tw-from-pulse-lime"
                              icon="pi pi-chart-bar"
                              iconColor="tw-text-pulse-lime"
                              iconBg="tw-bg-pulse-lime/20"
                              shadow="tw-shadow-[0_0_20px_rgba(102,160,68,0.3)]" />
                           <OverviewCard
                              mainText="Overall Uptime"
                              :subText="1"
                              gradientFrom="tw-from-pulse-green"
                              icon="pi pi-stopwatch"
                              iconColor="tw-text-pulse-green"
                              iconBg="tw-bg-pulse-green/20"
                              shadow="tw-shadow-[0_0_20px_rgba(34,197,94,0.3)]" />
                           <OverviewCard
                              mainText="Total Incidents"
                              :subText="1"
                              gradientFrom="tw-from-pulse-error"
                              icon="pi pi-exclamation-triangle"
                              iconColor="tw-text-pulse-error"
                              iconBg="tw-bg-pulse-error/20"
                              shadow="tw-shadow-[0_0_20px_rgba(239,68,68,0.3)]" />
                        </div>
                     </div>
                  </TabPanel>
</template>