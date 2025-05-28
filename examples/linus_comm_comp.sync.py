# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Kernel Breakdown Demo

# %%
from hta.trace_analysis import TraceAnalysis

# %% [markdown]
# ## Load traces

# %% [markdown]
# __<font color='red'>
# Note: To run the notebook, ensure that the path to the HolisticTraceAnalysis repo is set appropriately in the `trace_dir` variable below.
# </font>__

# %%
trace_prefix = "~/git/work/HolisticTraceAnalysis"
# trace_dir = f"{trace_prefix}/tests/data/vision_transformer/"
# trace_dir = f"{trace_prefix}/stack-trace-ddp/"
trace_dir = f"{trace_prefix}/jarl-trace/"
analyzer = TraceAnalysis(trace_dir=trace_dir)

# %% [markdown]
# ### Kernel Types
# Based on major event types we break down the kernels in three main categories. We refer to the following as kernel types.
# 1. COMPUTATION
# 1. COMMUNICATION
# 1. MEMORY (i.e., Memcpy from Device to Host, Host to Device etc.)
#
# ### Input
#
# The function takes the following parameters:
# - **duration_ratio**: float - a value between 0 and 1 representing the proportion of time taken by top COMM/COMP/MEMORY kernels. Default value = 0.8.
# - **num_kernels**: int - number of kernels to show for each category. Default value = 10.
# - **include_memory_kernels**: bool - whether to include the IO category or not. Default value = False.
# - **visualize**: bool - whether to show the plots or not. Default value = True.
# - **image_renderer**: str - image renderer to use. We use plotly to generate the graphs. The plots do not render in a notebook on github with the default rendering engine. Hence, we use "png" in the examples below.
#
# ### Output
# Dataframes
# 1. The first dataframe presents the percentage of time spent by each kernel type.
# 2. The second dataframe presents the min, max, mean, total(sum), time spent by each kernel along with its standard deviation.
#
# Visual Output
# - The Pie chart presents the percentage of time spent by each kernel type.
# - The Pie charts show the (COMM / COMP / MEMORY) kernels taking the most time on each rank.
# - The Bar plots show the average time taken by the longest kernels across all the ranks. In other words, it is the distribution of average time across the ranks.

# %% [markdown]
# __Note: Running the function in a notebook and hovering over the graphs will show relevant information such as kernel name, percentage of time taken by the kernel.__

# %% [markdown]
# ### Find the top five kernels by time for each kernel type 

# %%

# %%
kernel_type_metrics_df, kernel_metrics_df = analyzer.get_gpu_kernel_breakdown( 
                                             num_kernels=5, 
                                             include_memory_kernels=True, 
                                             image_renderer="png")

# %%
kernel_type_metrics_df

# %%

# %%

# %%
kernel_metrics_df

# %%
overlap_df = analyzer.get_comm_comp_overlap(visualize=True)

# %%
